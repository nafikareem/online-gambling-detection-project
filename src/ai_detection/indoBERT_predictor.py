import torch
from transformers import BertTokenizer, BertForSequenceClassification

class IndoBERTPredictor:
    def __init__(self, model_path):
        self.tokenizer = BertTokenizer.from_pretrained(model_path)
        self.model = BertForSequenceClassification.from_pretrained(model_path)
        self.model.eval()

    def predict(self, text):
        inputs = self.tokenizer(
            text,
            max_length=128,
            padding='max_length',
            truncation=True,
            return_tensors="pt"
        )
        with torch.no_grad():
            outputs = self.model(**inputs)
            logits = outputs.logits
            prediction = torch.argmax(logits, dim=1).item()
        return prediction

# Example usage
if __name__ == "__main__":
    predictor = IndoBERTPredictor('../../models/indoBERT')
    text = "Ini adalah komentar contoh."
    prediction = predictor.predict(text)
    print(f"Prediction: {prediction}")