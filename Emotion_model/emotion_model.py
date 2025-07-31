import torch.nn.functional as F
from transformers import AutoTokenizer, AutoModelForSequenceClassification
import torch
import json

class EmotionDetector:
    def __init__(self, model_name="SamLowe/roberta-base-go_emotions", config_path="config.json"):
        self.model = None
        self.tokenizer = None
        self.model_name = model_name
        self.config_path = config_path
        self.id2label = None


    def load_emotion_model(self):
        self.model = AutoModelForSequenceClassification.from_pretrained(self.model_name)
        self.model.eval()
        self.tokenizer = AutoTokenizer.from_pretrained(self.model_name)
        self.id2label = self.model.config.id2label

    def detect_emotion(self):
        with open(self.config_path, "r", encoding="utf-8") as f:
            config = json.load(f)
        response_file_path = config["last_response_path"]

        with open(response_file_path, "r", encoding="utf-8") as file:
            text = file.read().strip()

        inputs = self.tokenizer([text], return_tensors="pt", padding=True, truncation=True)

        with torch.no_grad():
            outputs = self.model(**inputs)
            logits = outputs.logits
            probs = F.softmax(logits, dim=-1)
            predicted_class_id = torch.argmax(probs, dim=-1)
            predicted_label = self.id2label[predicted_class_id.item()]
            return predicted_class_id, predicted_label