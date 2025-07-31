import whisper

class SpeechToTextModel():
    def __init__(self, model_name = "small"):
        self.model_name = model_name
        self.model = None

    def load_model(self):
        self.model = whisper.load_model(self.model_name)


    def process_speech_to_text(self, output):
        result = self.model.transcribe(output)
        return result["text"]
