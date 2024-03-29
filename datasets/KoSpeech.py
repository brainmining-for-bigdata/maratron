from concurrent.futures import ProcessPoolExecutor
from functools import partial
import numpy as np
import os
from util import audio
import librosa
from hparams import hparams


def build_from_path(in_dir, out_dir, num_workers=1, tqdm=lambda x: x):

  print('build_from_path.....')
  # We use ProcessPoolExecutor to parallelize across processes. This is just an optimization and you
  # can omit it and just call _process_utterance on each input if you want.
  executor = ProcessPoolExecutor(max_workers=num_workers)
  futures = []
  index = 0
  with open(os.path.join(in_dir, 'transcript.txt'), encoding='utf-8') as f:
    for line in f:
      parts = line.strip().split('|')
      titlePart = parts[0].split('/')
      wav_path = (os.path.join(in_dir, 'wavs', titlePart[1]))
      duration = librosa.get_duration(filename=wav_path)
      limit = 5* 20/1000*hparams.outputs_per_step*hparams.frame_shift_ms
      index += 1
      if (duration > limit ) :
        print('wav_path: ',wav_path, '\nduration:', duration)
        continue
      text = parts[2]
      futures.append(executor.submit(partial(_process_utterance, out_dir, index, wav_path, text)))
      # if index == 10: 
      #   break
  return [future.result() for future in tqdm(futures)]


def _process_utterance(out_dir, index, wav_path, text):
  '''Preprocesses a single utterance audio/text pair.

  This writes the mel and linear scale spectrograms to disk and returns a tuple to write
  to the train.txt file.

  Args:
    out_dir: The directory to write the spectrograms into
    index: The numeric index to use in the spectrogram filenames.
    wav_path: Path to the audio file containing the speech input
    text: The text spoken in the input audio file

  Returns:
    A (spectrogram_filename, mel_filename, n_frames, text) tuple to write to train.txt
  '''

  # Load the audio to a numpy array:
  print('wave_path :', wav_path)
  wav= audio.load_wav(wav_path)
  print('wav :', wav.shape, 'sr:')

  # Compute the linear-scale spectrogram from the wav:
  spectrogram = audio.spectrogram(wav).astype(np.float32)
  #print('spectrogram: ', spectrogram, '\nspectrogram,shape: ', spectrogram.shape)
  n_frames = spectrogram.shape[1]
  print('n_frames : ', n_frames)


  # Compute a mel-scale spectrogram from the wav:
  mel_spectrogram = audio.melspectrogram(wav).astype(np.float32)
  #print('melspectrogram: ', mel_spectrogram, '\nspectrogram,shape: ', mel_spectrogram.shape)

  # Write the spectrograms to disk:
  spectrogram_filename = 'KoSpeech-spec-%05d.npy' % index
  mel_filename = 'KoSpeech-mel-%05d.npy' % index
  print('spectrogram_filename:', spectrogram_filename)
  print('mel_filename:', mel_filename)
  print('out_dir: ', out_dir)
  np.save(os.path.join(out_dir, spectrogram_filename), spectrogram.T, allow_pickle=False)
  np.save(os.path.join(out_dir, mel_filename), mel_spectrogram.T, allow_pickle=False)

  # Return a tuple describing this training example:
  return (spectrogram_filename, mel_filename, n_frames, text)
