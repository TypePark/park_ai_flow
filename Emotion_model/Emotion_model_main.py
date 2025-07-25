from Emotion_model import EmotionDetector

if __name__ == '__main__':
    detector = EmotionDetector()
    detector.load_emotion_model()
    emotion = detector.detect_emotion()
    print(emotion)
