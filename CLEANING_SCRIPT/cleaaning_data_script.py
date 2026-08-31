""" Cleaning Data Script for Tweets Dataset """

import pandas as pd
 
INPUT_FILE = "Tweets.csv"
OUTPUT_FILE = "processed_tweets.csv"

""" This script reads the input CSV file, processes the data, and saves the cleaned data to a new CSV file. """
def main():
    # Load the dataset
    df = pd.read_csv(INPUT_FILE)

