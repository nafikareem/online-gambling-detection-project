import re
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from Sastrawi.Stemmer.StemmerFactory import StemmerFactory

# Inisialisasi stemmer Sastrawi
factory = StemmerFactory()
stemmer = factory.create_stemmer()

def preprocess_text(text):
    # Ubah ke huruf kecil
    text = text.lower()
    # Hapus tanda baca, emoji, dan karakter aneh
    text = re.sub(r'[^\w\s]', '', text)
    # Lemmatization menggunakan Sastrawi
    text = stemmer.stem(text)
    # Tokenisasi
    tokens = word_tokenize(text)
    # Hapus stopwords
    stop_words = set(stopwords.words('indonesian'))
    tokens = [word for word in tokens if word not in stop_words]
    # Gabungkan kembali
    return ' '.join(tokens)