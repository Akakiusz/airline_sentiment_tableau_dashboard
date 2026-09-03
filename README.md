# Airline Customer Sentiment Dashboard

An interactive Tableau dashboard exploring real, human-labeled customer sentiment
about six major US airlines, based on the Twitter US Airline Sentiment dataset.

## Live dashboard: (* once it's published on Tableau Public)

# What this is about
I wanted to build something that goes from raw data to a real, working dashboard — not just a notebook with a few charts. This project uses the Twitter US Airline Sentiment dataset, where each tweet is labeled as positive, negative, or neutral by a human annotator. Negative tweets also come with a specific reason (late flight, lost luggage, bad customer service, etc.), which lets me break down not just how many people were unhappy, but why.

# What's in the dashboard
Overall sentiment split, and how it differs airline by airline
What's actually driving negative feedback (top complaint reasons)
How sentiment shifts by day and hour
A filterable table so you can dig into individual tweets

# The data Source: 
Source: [Twitter US Airline Sentiment](https://www.kaggle.com/datasets/crowdflower/twitter-airline-sentiment) (Kaggle, originally collected by CrowdFlower/Figure Eight)
14,640 tweets about 6 airlines, labeled Feb 16–24, 2015
Sentiment and negative-reason labels are human-annotated, not inferred

## Known limitations
The dataset covers a single week in February 2015 — trends should be read at the
  day/hour level, not as a long-term pattern

# How it's built
CLEANING_SCRIPT/cleaaning_data_script.py — cleans the raw export, parses timestamps into date/hour/day-of-week, and writes DATASETS/processed_tweets.csv
That processed CSV gets loaded straight into Tableau
Dashboard built and published on Tableau Public