from flask import Flask, jsonify
from language_model import ModelChat
import requests

app = Flask(__name__)

model_chat = ModelChat()
model_chat.load_model()

@app.route("/chat", methods=["POST"])
def chat():
    print("Response processing")
    try:
        try:
            with open("last_user_input.txt", "r", encoding="utf-8") as f:
                user_input = f.read().strip()
        except FileNotFoundError:
            return jsonify({"error": "last_user_input.txt not found"}), 400

        if not user_input:
            return jsonify({"error": "Input file is empty"}), 400

        response = model_chat.chat(user_input)

        with open("last_response.txt", "w", encoding="utf-8") as f:
            f.write(response)

        try:
            requests.post("http://localhost:5002/emotion")
        except requests.exceptions.RequestException as e:
            print(f"Emotion service error: {e}")

        try:
            requests.post("http://localhost:5004/tts")
        except requests.exceptions.RequestException as e:
            print(f"TTS service error: {e}")

        try:
            godot_url = "http://localhost:5010/update"
            payload = {"response": response}
            requests.post(godot_url, json=payload, timeout=30)
            print("Successfully pushed update to Godot.")
        except requests.exceptions.RequestException as e:
            print(f"Could not push update to Godot (is the game running?): {e}")

        return jsonify({"response": response})

    except Exception as e:
        return jsonify({"error": str(e)}), 500


if __name__ == "__main__":
    app.run(port=5001)
