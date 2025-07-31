from flask import Flask, jsonify
from speech_to_speech import SpeechToSpeech

app = Flask(__name__)

sts = SpeechToSpeech()
sts.load_sts_model()

@app.route("/sts", methods=["POST"])
def process_speech():
    try:
        sts.process_audio()
        return jsonify("Audio processed successfully")
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(port=5005)
