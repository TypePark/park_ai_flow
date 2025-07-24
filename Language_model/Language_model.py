import json
from llama_cpp import Llama

class ModelChat:
    def __init__(self, config_path="Language_model/config.json"):
        self.llm = None
        self.chat_history = "### System:\nYou are a helpful assistant.\n"
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
        prompt = self.chat_history + f"\n### User:\n{user_input}\n### Assistant:\n"
        response = self.llm(
            prompt=prompt,
            max_tokens=300,
            stop=["### User:", "### Assistant:"],
            temperature=0.7
        )
        answer = response["choices"][0]["text"].strip()
        self.chat_history += f"\n### User:\n{user_input}\n### Assistant:\n{answer}"
        return answer
