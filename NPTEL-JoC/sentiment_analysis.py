"""
A sentiment analysis script that processes text data from an Excel file using NLTK's VADER sentiment analyzer.

This script reads text data from a specified Excel file, analyzes the sentiment of each text entry
using NLTK's VADER (Valence Aware Dictionary and sEntiment Reasoner) sentiment analyzer, and
prints detailed sentiment scores for each entry.

The sentiment scores include:
- neg: Negative sentiment score (0 to 1)
- neu: Neutral sentiment score (0 to 1)
- pos: Positive sentiment score (0 to 1)
- compound: Normalized compound score (-1 to 1)

Requirements:
    - nltk
    - pandas
    - Excel file with a 'Text' column in 'Sheet1'

Input file format:
    Excel file (.xlsx) with:
    - Sheet name: 'Sheet1'
    - Column name: 'Text'

Example output:
    Test Data 1...
    "I am happy" : {'neg': 0.0, 'neu': 0.0, 'pos': 1.0, 'compound': 0.5719}
    neg : 0.0
    neu : 0.0
    pos : 1.0
    compound : 0.5719

"""

import nltk
import pandas as pd
from nltk.sentiment.vader import SentimentIntensityAnalyzer

nltk.download("vader_lexicon")

file_path = "data/sentiment_input_data.xlsx"
excel_data = pd.ExcelFile(file_path)
dataframe = excel_data.parse("Sheet1")  # Parse the sheet to DF
dataframe = dataframe.dropna()  # Drop rows with NaN values
dataframe = list(dataframe["Text"])  # Convert DF to list

sentiment_analyzer = SentimentIntensityAnalyzer()
for idx, data in enumerate(dataframe, start=1):
    print(f"Test Data {idx}...")
    sentiment_score = sentiment_analyzer.polarity_scores(data)
    print(data, ":", sentiment_score)
    for key in sentiment_score:
        print(key, ":", sentiment_score[key])
    print("\n")
