# Spam Detection Project

This project aims to identify online gambling advertisements in social media comments using a combination of keyword filtering and AI-based detection methods.

## Project Structure

```
online-gambling-detection-project
├── data
│   ├── raw
│   │   └── final.xlsx                   # Raw data of social media comments
│   ├── processed
│       └── cleaned_comments.csv         # Processed comments ready for analysis
├── models
│   ├── keyword_filtering.py             # Implements keyword filtering logic
│   ├── ai_detection.py                  # Contains AI-based detection logic
│   └── model.pkl                        # Serialized model for AI detection
├── notebooks
│   └── preprocessing.ipynb              # Jupyter notebook for data preprocessing
├── src
│   ├── main.py                          # Entry point of the application
│   ├── utils
│   │   ├── data_loader.py               # Functions for loading data from CSV files
│   │   ├── text_preprocessing.py        # Functions for text preprocessing
│   │   └── evaluation.py                 # Functions for evaluating model performance
│   ├── keyword_filtering
│   │   └── filter_keywords.py           # Implementation of keyword filtering logic
│   └── ai_detection
│       └── indoBERT_predictor.py
│       └── train_indoBERT.py            # Logic for training the AI model
├── tests
├── requirements.txt                     # Lists dependencies required for the project
├── README.md                            # Documentation for the project
└── .gitignore                           # Specifies files to be ignored by version control
```

## Installation

1. Clone the repository:
   ```
   git clone <repository-url>
   cd spam-detection-project
   ```

2. Install the required dependencies:
   ```
   pip install -r requirements.txt
   ```

## Usage

1. Prepare your dataset by placing the raw social media comments in `data/raw/social_media_comments.csv`.

2. Run the preprocessing notebook to clean and prepare the data:
   ```
   jupyter notebook notebooks/preprocessing.ipynb
   ```

3. Use the `main.py` file to initialize the keyword filtering and AI detection processes:
   ```
   python src/main.py
   ```

## Features

- **Keyword Filtering**: Filters comments based on predefined keywords related to online gambling.
- **AI Detection**: Utilizes a trained AI model to predict whether a comment is spam or not.
- **Data Preprocessing**: Includes functions for cleaning and normalizing text data.

## Contributing

Contributions are welcome! Please open an issue or submit a pull request for any improvements or bug fixes.

## License

This project is licensed under the MIT License. See the LICENSE file for details.