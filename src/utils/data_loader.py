import pandas as pd

def load_raw_data(file_path):
    return pd.read_excel(file_path)

def load_cleaned_data(file_path):
    return pd.read_csv(file_path)