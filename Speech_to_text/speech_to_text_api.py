from flask import Flask, jsonify
from speech_to_text import push_to_talk
import requests
from speech_to_text_model import SpeechToTextModel


app = Flask(__name__)

@app.route("/stt", methods=["POST"])
def transcribe():
    push_to_talk()
    return jsonify("Done")

if __name__ == "__main__":
    app.run(port=5003)