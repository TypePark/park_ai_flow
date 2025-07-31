from flask import Flask, jsonify
from emotion_model import EmotionDetector

app = Flask(__name__)

emotion_detector = EmotionDetector()
emotion_detector.load_emotion_model()

@app.route("/emotion", methods=["POST"])
def get_emotion():
    try:
        class_id, label = emotion_detector.detect_emotion()
        print(label)

        return jsonify({"predicted_class_id": class_id.item(), "predicted_label": label})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(port=5002)
