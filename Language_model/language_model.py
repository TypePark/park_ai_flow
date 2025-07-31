import json
from llama_cpp import Llama

class ModelChat:
    def __init__(self, config_path="config.json"):
        self.llm = None
        self.chat_history = "You are Neko‑chan, a playful cat‑girl. You speak with occasional 'meow!', gentle purrs, and a cheerful tone."
        self.config_path = config_path

    def load_model(self):
        with open(self.config_path, "r") as f:
            config = json.load(f)
        model_path = config["model_path"]

        self.llm = Llama(
            model_path=model_path,
            n_ctx=2048,
            n_gpu_layers=10,
            verbose=True
        )
        print("Model loaded successfully.")

    def chat(self, user_input):
        prompt = f"{self.chat_history}\nUser: {user_input}\nAssistant:"
        response = self.llm(
            prompt=prompt,
            max_tokens=300,
            stop=["User:", "Assistant:"],
            temperature=0.7
        )
        answer = response["choices"][0]["text"].strip()
        self.chat_history += f"\nUser: {user_input}\nAssistant: {answer}"
        return answer

