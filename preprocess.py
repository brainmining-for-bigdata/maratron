import argparse
import os
from multiprocessing import cpu_count
from tqdm import tqdm
from datasets import blizzard, ljspeech, california , ljspeech_ko , KoSpeech
from hparams import hparams


def preprocess_blizzard(args):
  in_dir = os.path.join(args.base_dir, 'Blizzard2012')
  out_dir = os.path.join(args.base_dir, args.output)
  os.makedirs(out_dir, exist_ok=True)
  metadata = blizzard.build_from_path(in_dir, out_dir, args.num_workers, tqdm=tqdm)
  write_metadata(metadata, out_dir)

def preprocess_ljspeech(args):
  in_dir = os.path.join(args.base_dir, 'LJSpeech-1.1')
  print('in_dir : ', in_dir)
  out_dir = os.path.join(args.base_dir, args.output)
  print('out_dir : ', out_dir)
  os.makedirs(out_dir, exist_ok=True)
  metadata = ljspeech.build_from_path(in_dir, out_dir, args.num_workers, tqdm=tqdm)
  write_metadata(metadata, out_dir)

def preprocess_ljspeech_ko(args):
  in_dir = os.path.join(args.base_dir, 'ljspeech_ko')
  print('in_dir : ', in_dir)
  out_dir = os.path.join(args.base_dir, args.output)
  print('out_dir : ', out_dir)
  os.makedirs(out_dir, exist_ok=True)
  metadata = ljspeech_ko.build_from_path(in_dir, out_dir, args.num_workers, tqdm=tqdm)
  write_metadata(metadata, out_dir)

def preprocess_california(args):
  in_dir = os.path.join(args.base_dir,  'california')
  print(args.base_dir)
  print(in_dir)
  out_dir = os.path.join(args.base_dir, args.output)
  os.makedirs(out_dir, exist_ok=True)
  metadata = california.build_from_path(in_dir, out_dir, args.num_workers, tqdm=tqdm)
  write_metadata(metadata, out_dir)

def preprocess_KoSpeech(args):
  in_dir = os.path.join(args.base_dir, 'KoSpeech')
  print('in_dir : ', in_dir)
  out_dir = os.path.join(args.base_dir, args.output)
  print('out_dir : ', out_dir)
  os.makedirs(out_dir, exist_ok=True)
  metadata = KoSpeech.build_from_path(in_dir, out_dir, args.num_workers, tqdm=tqdm)
  write_metadata(metadata, out_dir)

def write_metadata(metadata, out_dir):
  with open(os.path.join(out_dir, 'train.txt'), 'w', encoding='utf-8') as f:
    for m in metadata:
      f.write('|'.join([str(x) for x in m]) + '\n')
  frames = sum([m[2] for m in metadata])
  hours = frames * hparams.frame_shift_ms / (3600 * 1000)
  print('Wrote %d utterances, %d frames (%.2f hours)' % (len(metadata), frames, hours))
  print('Max input length:  %d' % max(len(m[3]) for m in metadata))
  print('Max output length: %d' % max(m[2] for m in metadata))


def main():
  print('initializing preprocessing..')
  parser = argparse.ArgumentParser()
  # 현재 작업중인 directory알아내기
  print("dirname:\t" + os.path.dirname(os.path.abspath(__file__)))
  print("getcwd:\t\t" + os.getcwd())
  #parser.add_argument('--base_dir', default=os.path.expanduser('~/tacotron'))
  parser.add_argument('--base_dir', default=os.getcwd())
  parser.add_argument('--output', default='training')
  parser.add_argument('--dataset', required=True, choices=['blizzard', 'ljspeech', 'california', 'KoSpeech' , 'ljspeech_ko'])
  parser.add_argument('--num_workers', type=int, default=cpu_count())
  parser.add_argument('--hparams', default='',        ## modified hparams if neccessary
                      help='Hyperparameter overrides as a comma-separated list of name=value pairs')
  parser.add_argument('--language', default='en_US')
  parser.add_argument('--voice', default='female')
  parser.add_argument('--reader', default='mary_ann')
  parser.add_argument('--merge_books', default='False')
  parser.add_argument('--book', default='northandsouth')
  args = parser.parse_args()
  # modified_hp = hparams.parse(args.hparams)
  # assert args.merge_books in ('False', 'True')                    # add contrain to merge_book param
  # args = parser.parse_args()
  if args.dataset == 'blizzard':
    preprocess_blizzard(args)
  elif args.dataset == 'ljspeech':
    preprocess_ljspeech(args)
  elif args.dataset == 'ljspeech_ko':
    preprocess_ljspeech_ko(args)
  elif args.dataset == 'KoSpeech':
    preprocess_KoSpeech(args)
  elif args.dataset == 'california':
    preprocess_california(args)
    

if __name__ == "__main__":
  main()
