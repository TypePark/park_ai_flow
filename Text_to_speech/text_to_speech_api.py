from flask import Flask, jsonify
from text_to_speech import TextToSpeech
import requests

app = Flask(__name__)

tts = TextToSpeech()
tts.load_model_tts()

@app.route("/tts", methods=["POST"])
def tts_api():
    tts.process_text_output()

    try:
        requests.post("http://localhost:5005/sts")

    except requests.exceptions.RequestException as e:
        print(f"Emotion service error {e}")

    return jsonify("Done")


if __name__ == "__main__":
    app.run(port=5004)
