import re
import unicodedata
from argparse import ArgumentParser
from pathlib import Path

import soundfile as sf

from .hifigan.mel2wave import mel2wave
from .nat.config import FLAGS
from .nat.text2mel import text2mel

class TextToSpeech:
  def __init__(self) -> None:
      self.sample_rate = 16000
      self.silence_duration = 0.2
      self.lexicon_file = "assets/infore/lexicon.txt"


  def nat_normalize_text(self,text):
    text = unicodedata.normalize('NFKC', text)
    text = text.lower().strip()
    sp = FLAGS.special_phonemes[FLAGS.sp_index]
    text = re.sub(r'[\n.,:]+', f' {sp} ', text)
    text = text.replace('"', " ")
    text = re.sub(r'\s+', ' ', text)
    text = re.sub(r'[.,:;?!]+', f' {sp} ', text)
    text = re.sub('[ ]+', ' ', text)
    text = re.sub(f'( {sp}+)+ ', f' {sp} ', text)
    return text.strip()

  def return_clip(self,text,output):
    text = self.nat_normalize_text(text)
    print('Normalized text input:', text)
    mel = text2mel(text, self.lexicon_file, self.silence_duration)
    wave = mel2wave(mel)
    print('writing output to file', output)
    sf.write(str(output), wave, samplerate=self.sample_rate)
