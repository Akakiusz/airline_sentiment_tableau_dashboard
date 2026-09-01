""" Cleaning Data Script for Tweets Dataset """

import pandas as pd
 
INPUT_FILE = "Tweets.csv"
OUTPUT_FILE = "processed_tweets.csv"

""" This script reads the input CSV file, processes the data, and saves the cleaned data to a new CSV file. """
def main():
    # Load the dataset
    df = pd.read_csv(INPUT_FILE)

 """ Convert the 'tweet_created' column to datetime and extract date, hour, and day of the week. """
    df["tweet_created"] = pd.to_datetime(df["tweet_created"])
    df["Date"] = df["tweet_created"].dt.date
    df["Hour"] = df["tweet_created"].dt.hour
    df["Day of week"] = df["tweet_created"].dt.day_name()
 
    df["negativereason"] = df["negativereason"].fillna("Not applicable")

 """ Select relevant columns and rename them for clarity. """
    keep_cols = {
        "tweet_id": "Tweet ID",
        "airline_sentiment": "Sentiment",
        "airline_sentiment_confidence": "Sentiment confidence",
        "negativereason": "Negative reason",
        "airline": "Airline",
        "text": "Tweet text",
        "Date": "Date",
        "Hour": "Hour",
        "Day of week": "Day of week",
        "retweet_count": "Retweet count",
    }

""" Create a new DataFrame with the selected columns and save it to a CSV file. """
    out = df[list(keep_cols.keys())].rename(columns=keep_cols)
    out.to_csv(OUTPUT_FILE, index=False)
 
""" Print summary statistics about the processed data. """
    print(f"Rows processed: {len(out)}")
    print(out["Sentiment"].value_counts())
    print(f"Date range: {df['tweet_created'].min()} to {df['tweet_created'].max()}")
    print(f"Saved -> {OUTPUT_FILE}")
 
 """ Entry point of the script. """
if __name__ == "__main__":
    main()