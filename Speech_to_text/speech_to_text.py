from record_voice import Recorder
from speech_to_text_model import SpeechToTextModel
import keyboard
import requests

sttm = SpeechToTextModel()
sttm.load_model()

rec = Recorder()

def stop_and_transcribe(something):
    rec.record_stop(something)
    print(" Transcribing")

    text_user = sttm.process_speech_to_text(rec.output_file)
    print(text_user)
    with open("last_user_input.txt", "w", encoding="utf-8") as f:
        f.write(text_user)

    try:
        requests.post("http://localhost:5001/chat")
    except requests.exceptions.RequestException as e:
        print(f"Language model service error: {e}")


def push_to_talk():
    keyboard.on_press_key("v", rec.record_start)
    keyboard.on_release_key("v", stop_and_transcribe)

    try:
        keyboard.wait()
    except KeyboardInterrupt:
        rec.cleanup()
        print("Stopped.")

if __name__ == "__main__":
    push_to_talk()
