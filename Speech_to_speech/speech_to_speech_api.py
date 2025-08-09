import requests
from flask import Flask, jsonify
from speech_to_speech import SpeechToSpeech

app = Flask(__name__)

sts = SpeechToSpeech()
sts.load_sts_model()

@app.route("/sts", methods=["POST"])
def process_speech():
    try:
        sts.process_audio()

        try:
            godot_url = "http://localhost:5011"
            payload = {"audio_name": "last_voice_output_sts.wav"}
            requests.post(godot_url, json=payload, timeout=30)
            print("Successfully pushed update to Godot.")

        except requests.exceptions.RequestException as e:
            print(f"Could not push update to Godot (is the game running?): {e}")
        return jsonify("Audio processed successfully.")

    except Exception as e:
        print(f"An error occurred during audio processing: {e}")
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(port=5005)
