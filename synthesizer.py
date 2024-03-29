import io
import numpy as np
import tensorflow as tf
from hparams import hparams
from librosa import effects
from models import create_model
from text import text_to_sequence
from KoTextProcessing.HangulUtils import hangul_to_sequence
from util import audio
import re
import sys
import nltk



class Synthesizer:
  def load(self, checkpoint_path, model_name='tacotron'):
    print('Constructing model: %s' % model_name)
    inputs = tf.placeholder(tf.int32, [1, None], 'inputs')
    input_lengths = tf.placeholder(tf.int32, [1], 'input_lengths')
    with tf.variable_scope('model') as scope:
      self.model = create_model(model_name, hparams)
      self.model.initialize(inputs, input_lengths)
      self.wav_output = audio.inv_spectrogram_tensorflow(self.model.linear_outputs[0])

    print('Loading checkpoint: %s' % checkpoint_path)
    self.session = tf.Session()
    self.session.run(tf.global_variables_initializer())
    self.saver = tf.train.Saver()
    self.saver.restore(self.session, checkpoint_path)

  def reload(self, checkpoint_path, model_name='tacotron'):
    self.session.close()
    tf.reset_default_graph ()
    self.load(checkpoint_path, model_name='tacotron')

  def tokenize (self, text , cleaner_name) :
    if cleaner_name == 'korean_cleaners':
      # hangul = re.compile('[^ ,.?ㄱ-ㅣ가-힣]+')
      # Ko_text = hangul.sub(' ', text) 
      # Ko_text = text.replace(',','.').replace('?','.')
      # texts = Ko_text.split('.')
      # for i in texts:
      #   sentence = i + '.'
      # tokenizer = nltk.data.load('text/punkt/english.pickle')
      tokenizer = nltk.data.load('tokenizers/punkt/english.pickle')
      sentence = tokenizer.tokenize(text)

    elif cleaner_name == 'english_cleaners':
      # tokenizer = nltk.data.load('text/punkt/english.pickle')
      tokenizer = nltk.data.load('tokenizers/punkt/english.pickle')
      sentence = tokenizer.tokenize(text)

    for i in range(0,len(sentence)) :
      if len(sentence[i]) == 0 or sentence[i] == ' ' :
        del sentence[i]
    return sentence

  def synthesize(self, text):
    cleaner_names = [x.strip() for x in hparams.cleaners.split(',')]
    print ('***cleaner_names:', cleaner_names)
    print ('***text:', text)
    texts = self.tokenize(text,cleaner_names[0])
    print(texts)
    waves=[]

    for text in texts:
      if cleaner_names[0] == 'english_cleaners' :
        seq = text_to_sequence(text, cleaner_names)
        print (' text:{}\n seq{}:'.format( text,seq))
      elif cleaner_names[0] == 'korean_cleaners' :
        seq = hangul_to_sequence(text, cleaner_names)
        print (' text:{}\n seq{}:'.format( text,seq))

      feed_dict = {
        self.model.inputs: [np.asarray(seq, dtype=np.int32)],
        self.model.input_lengths: np.asarray([len(seq)], dtype=np.int32)
      }
      wav = self.session.run(self.wav_output, feed_dict=feed_dict)
      wav = audio.inv_preemphasis(wav)
      wav = wav[:audio.find_endpoint(wav)]
      waves.append(wav)  
      

    wavestack=waves[0]
    for wave in waves[1:]:
      wavestack=np.hstack((wavestack,wave))  
    out = io.BytesIO()
    audio.save_wav(wavestack, out)
    return out.getvalue()
