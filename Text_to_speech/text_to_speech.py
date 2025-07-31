from kokoro import KPipeline
from IPython.display import display, Audio
import soundfile as sf
import json


class TextToSpeech:
    def __init__(self, config_path="config.json"):
        self.config_path = config_path
        self.pipeline = KPipeline(lang_code="a")
        self.text = ""

    def load_model_tts(self):
        generator = self.pipeline(
            self.text, voice='af_heart',  # <= change voice here
            speed=1, split_pattern=r'\n+'
        )
        return generator

    def process_text_output(self):
        with open(self.config_path, "r", encoding="utf-8") as f:
            config = json.load(f)
        response_file_path = config["last_response_path"]

        with open(response_file_path, "r", encoding="utf-8") as file:
            self.text = file.read().strip()

        generator = self.load_model_tts()

        for i, (gs, ps, audio) in enumerate(generator):
            print(i)  # i => index
            print(gs)  # gs => graphemes/text
            print(ps)  # ps => phonemes
            display(Audio(data=audio, rate=24000, autoplay=i == 0))
            sf.write("last_voice_output_tts.wav", audio, 24000)
