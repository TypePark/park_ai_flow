import whisper

model = whisper.load_model("small")

def stt(output):
    result = model.transcribe(output)
    return result["text"]
