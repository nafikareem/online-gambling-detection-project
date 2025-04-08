import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import pandas as pd
from models.keyword_filtering import KeywordFilter
from models.ai_detection import AIDetector
from utils.data_loader import load_cleaned_data
from sklearn.metrics import accuracy_score, classification_report


def main():
    # Load cleaned comments dataset
    cleaned_comments = load_cleaned_data('C:/Users/MSI/OneDrive/Dokumen/Data Mining/online-gambling-detection-project/data/processed/cleaned_comments.csv')
    
    # Ensure 'processed_text' column is of string type and handle NaN values
    cleaned_comments['processed_text'] = cleaned_comments['processed_text'].fillna('').astype(str)
    
    # Initialize keyword filter and AI detector
    keyword_filter = KeywordFilter()
    keyword_filter.load_keywords('../data/keywords.txt')
    ai_detector = AIDetector()
    ai_detector.load_model('C:/Users/MSI/OneDrive/Dokumen/Data Mining/online-gambling-detection-project/models/indoBERT')

    # Allow user to input text for classification
    while True:
        user_input = input("Masukkan teks untuk diklasifikasikan (atau ketik 'exit' untuk keluar): ").strip()
        if user_input.lower() == 'exit':
            print("Keluar dari program.")
            break

        # Preprocess user input
        processed_text = user_input.lower().strip()
        processed_text = " ".join(processed_text.split())  # Menghapus spasi berlebih

        # Debugging: Print processed text
        print(f"Processed Text: {processed_text}")

        # Check with keyword filter
        keyword_detected = keyword_filter.is_gambling_related(processed_text)
        ai_prediction = ai_detector.predict([processed_text])[0]

        # Combine results
        if ai_prediction:
            print("Prediksi: Mengandung unsur judi (berdasarkan model AI).")
        elif keyword_detected:
            print("Prediksi: Bersih (tidak mengandung unsur judi, diverifikasi oleh model AI).")
        else:
            print("Prediksi: Bersih (tidak mengandung unsur judi).")


if __name__ == "__main__":
    main()