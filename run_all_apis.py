import subprocess

processes = [
    subprocess.Popen(["./venv-sts/bin/python", "Speech_to_speech/speech_to_speech_api.py"]),
    subprocess.Popen(["./.venv/bin/python", "Language_model/language_model_api.py"]),
    subprocess.Popen(["./.venv/bin/python", "Emotion_model/emotion_model_api.py"]),
    subprocess.Popen(["./venv-tts/bin/python", "Text_to_speech/text_to_speech_api.py"]),
    subprocess.Popen([
        "kitty", "--detach", "sudo", "./venv-stt/bin/python", "Speech_to_text/speech_to_text_api.py" # change "kitty" with the terminal you use.
    ])
]

try:
    for p in processes:
        p.wait()
except KeyboardInterrupt:
    print("Shutting down APIs")
    for p in processes:
        p.terminate()

