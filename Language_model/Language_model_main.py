import Language_model
import keyboard

from Emotion_model.Emotion_model import EmotionDetector

from Speech_to_text.Record_voice import Recorder
from Speech_to_text.speech_to_text_model import stt

rec = Recorder()
is_responding = False

emotiondetector = EmotionDetector()
emotiondetector.load_emotion_model()

model_chat = Language_model.ModelChat()
model_chat.load_model()


def stop_and_respond(something):
    global is_responding
    if is_responding:
        print("Please wait, still responding...")
        return

    is_responding = True
    try:
        rec.record_stop(something)
        text = stt(rec.output_file)
        print("You:", text)
        response = model_chat.chat(text)
        print("Assistant:", response)

        with open("last_response.txt", "w", encoding="utf-8") as f:
            f.write(response)
        emotion = emotiondetector.detect_emotion()
        print(emotion)


    except Exception as e:
        print("Error:", e)
    finally:
        is_responding = False

keyboard.on_press_key("v", rec.record_start)
keyboard.on_release_key("v", stop_and_respond)

try:
    print("Press and hold 'V' to talk...")
    keyboard.wait()
except KeyboardInterrupt:
    rec.cleanup()
    print("Stopped.")