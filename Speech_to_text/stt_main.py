from Record_voice import Recorder
from speech_to_text_model import stt
import keyboard

rec = Recorder()

def stop_and_transcribe(something):
    rec.record_stop(something)
    print("Transcribing")
    text = stt(rec.output_file)
    print(text)


keyboard.on_press_key("v", rec.record_start)
keyboard.on_release_key("v", stop_and_transcribe)

try:
    keyboard.wait()
except KeyboardInterrupt:
    rec.cleanup()
    print("Stopped.")
