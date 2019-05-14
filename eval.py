import argparse
import os
import re
from hparams import hparams, hparams_debug_string
from synthesizer import Synthesizer

'''sentences = [
  # From July 8, 2017 New York Times:
  'Scientists at the CERN laboratory say they have discovered a new particle.',
  'There’s a way to measure the acute emotional intelligence that has never gone out of style.',
  'President Trump met with other leaders at the Group of 20 conference.',
  'The Senate\'s bill to repeal and replace the Affordable Care Act is now imperiled.',
  # From Google's Tacotron example page:
  'Generative adversarial network or variational auto-encoder.',
  'The buses aren\'t the problem, they actually provide a solution.',
  'Does the quick brown fox jump over the lazy dog?',
  'Talib Kweli confirmed to AllHipHop that he will be releasing an album in the next year.',
]'''


class Eval :
  def init(self):
    os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'
    hparams.parse('')
    print(hparams_debug_string())
    self.voice_choice = hparams.voice_choice # female default
    self.base_dir = os.getcwd()
    self.synth = Synthesizer()
    self.output_path = os.path.join (self.base_dir, 'static', 'audio', 'output.wav')
    checkpoint= os.path.join(self.base_dir, 'LJlogs-tacotron', 'model.ckpt-40000')
    hparams.cleaners = 'english_cleaners'
    self.synth.load(checkpoint)



  # ['english_cleaners','korean_cleaners']
  def reload_checkpoint(self, voice_choice) :
    self.voice_choice = voice_choice
    if voice_choice == 1 :
      checkpoint= os.path.join(self.base_dir, 'LJlogs-tacotron', 'model.ckpt-40000')
      hparams.cleaners = 'english_cleaners'
      print ('Synthesizing: %s' % checkpoint)
      # self.synth.load(checkpoint)
      self.synth.reload(checkpoint)
    elif voice_choice == 2 :
      checkpoint = os.path.join(self.base_dir, 'california-12-logs', 'model.ckpt-112000')
      hparams.cleaners = 'english_cleaners'
      print ('Synthesizing: %s' % checkpoint)
      # self.synth.load(checkpoint)
      self.synth.reload(checkpoint)
    else :
      checkpoint = os.path.join(self.base_dir, 'logs-tacotron-model', 'model.ckpt-64000')
      hparams.cleaners = 'korean_cleaners'
      print ('Synthesizing: %s' % checkpoint)
      # self.synth.load(checkpoint)
      self.synth.reload(checkpoint)
    
    # self.voice_choice = voice_choice
    # print ('Synthesizing: %s' % checkpoint)
    # self.synth.reload(checkpoint)
    

  def text(self, text, voice_choice):
    print ('voice changed to  ', voice_choice)
    print(self.voice_choice)
    print(voice_choice)
    if self.voice_choice != voice_choice : 
      self.reload_checkpoint (voice_choice)
    return (self.synth.synthesize(text))
    '''
    with open(self.output_path, 'wb') as f:
      f.write(self.synth.synthesize(text))
    return os.path.basename(self.output_path)
    '''
    
def get_output_base_path(checkpoint_path):
  base_dir = os.path.dirname(checkpoint_path)
  m = re.compile(r'.*?\.ckpt\-([0-9]+)').match(checkpoint_path)
  name = 'eval-%d' % int(m.group(1)) if m else 'eval'
  return os.path.join(base_dir, name)

    

def run_eval(args):
  hparams.cleaners = args.cleaners
  print(hparams_debug_string())
  synth = Synthesizer()
  synth.load(args.checkpoint)
  if (args.audiobook) :
    with open(args.audiobook, encoding='utf-8') as f:
      data = f.read()
    parts = data.strip().split('|')
    title=parts[0]
    author=parts[1]
    text=parts[2]
    outpath= args.audiobook.replace(".txt", ".wav")
    with open(outpath, 'wb') as f:
      f.write(synth.synthesize(text))
  else: 
    base_path = get_output_base_path(args.checkpoint)
    for i, text in enumerate(sentences):
      path = '%s-%d.wav' % (base_path, i)
      print('Synthesizing: %s' % path)
      with open(path, 'wb') as f:
        f.write(synth.synthesize(text))


def main():
  parser = argparse.ArgumentParser()
  parser.add_argument('--checkpoint', required=True, help='Path to model checkpoint')
  parser.add_argument('--hparams', default='',
    help='Hyperparameter overrides as a comma-separated list of name=value pairs')

  parser.add_argument('--cleaners', default='english_cleaners')
  parser.add_argument('--audiobook', default='')

  args = parser.parse_args()
  os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'
  hparams.parse(args.hparams)
  run_eval(args)


if __name__ == '__main__':
  main()