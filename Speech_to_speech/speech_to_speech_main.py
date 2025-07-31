from speech_to_speech import SpeechToSpeech

def main():
    sts = SpeechToSpeech()
    sts.load_sts_model()
    sts.process_audio()

if __name__ == "__main__":
    main()
