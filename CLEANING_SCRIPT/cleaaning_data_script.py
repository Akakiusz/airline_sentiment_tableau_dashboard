# Cleaning Data Script for Tweets Dataset
#
# Reads the raw Twitter US Airline Sentiment export, cleans it up,
# and saves a processed CSV ready to import into Tableau.
# Sentiment labels are already human-annotated in the source data --
# this script does not classify anything, just cleans and adds fields.
 
import pandas as pd
 
INPUT_FILE = "Tweets.csv"
OUTPUT_FILE = "processed_tweets.csv"
 
 
def main():
    # Load the dataset
    df = pd.read_csv(INPUT_FILE)
 
    # Convert the 'tweet_created' column to datetime and extract date, hour, and day of the week.
    df["tweet_created"] = pd.to_datetime(df["tweet_created"])
    df["Date"] = df["tweet_created"].dt.date
    df["Hour"] = df["tweet_created"].dt.hour
    df["Day of week"] = df["tweet_created"].dt.day_name()
 
    # Tweets that aren't negative have no negative reason -- label them clearly instead of leaving blanks.
    df["negativereason"] = df["negativereason"].fillna("Not applicable")
 
    # Select relevant columns and rename them for clarity.
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
    out = df[list(keep_cols.keys())].rename(columns=keep_cols)
    out.to_csv(OUTPUT_FILE, index=False)
 
    # Print a quick summary so you can confirm the script ran correctly.
    print(f"Rows processed: {len(out)}")
    print(out["Sentiment"].value_counts())
    print(f"Date range: {df['tweet_created'].min()} to {df['tweet_created'].max()}")
    print(f"Saved -> {OUTPUT_FILE}")
 
 
if __name__ == "__main__":
    main()
 