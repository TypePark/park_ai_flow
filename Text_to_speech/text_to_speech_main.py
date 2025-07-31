from text_to_speech import TextToSpeech

def main():
    tts = TextToSpeech()
    tts.load_model_tts()
    tts.process_text_output()

if __name__ == "__main__":
    main()
