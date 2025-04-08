import torch
from transformers import BertTokenizer, BertForSequenceClassification
import os

class AIDetector:
    def __init__(self):
        self.model = None
        self.tokenizer = None

    def load_model(self, model_path='../../models/model_indoBERT'):
        if not os.path.exists(model_path):
            raise FileNotFoundError(f"Model folder '{model_path}' tidak ditemukan.")
        self.model = BertForSequenceClassification.from_pretrained(model_path)
        self.tokenizer = BertTokenizer.from_pretrained(model_path)

    def predict(self, comments):
        if self.model is None or self.tokenizer is None:
            raise ValueError("Model belum dimuat. Panggil load_model terlebih dahulu.")
        predictions = []
        for comment in comments:
            encoding = self.tokenizer(comment, truncation=True, padding=True, max_length=128, return_tensors='pt')
            with torch.no_grad():
                outputs = self.model(**encoding)
                prediction = torch.argmax(outputs.logits, dim=1).item()
            predictions.append(prediction)
        return predictions