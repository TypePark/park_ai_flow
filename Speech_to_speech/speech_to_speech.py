from pathlib import Path
from dotenv import load_dotenv
from scipy.io import wavfile
from rvc.modules.vc.modules import VC

class SpeechToSpeech:
      def __init__(self, vc = VC()):
            self.vc = vc

      def load_sts_model(self):
            load_dotenv(".env")
            self.vc.get_vc("model.pth")

      def process_audio(self):
            tgt_sr, audio_opt, times, _ = self.vc.vc_inference(1, Path("last_voice_output_tts.wav"))
            wavfile.write("last_voice_output_sts.wav", tgt_sr, audio_opt)


