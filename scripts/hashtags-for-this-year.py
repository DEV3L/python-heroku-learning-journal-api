import json
import os
from datetime import datetime

from dotenv import load_dotenv

from src.extractors.time_extractor import TimeExtractor

load_dotenv()

DATA_SEED_TWITTER_PATH = os.environ.get('DATA_SEED_TWITTER_PATH', './data/tweet.json')

current_year = datetime.today().year

if __name__ == '__main__':
    with open(DATA_SEED_TWITTER_PATH) as data_seed:
        data = json.load(data_seed)

    time_extractor = TimeExtractor(data)
    tweets_from_this_year = time_extractor.tweets_for_year(current_year)

    hashtag_set = set()
    for tweet in tweets_from_this_year:
        hashtags = [hashtag_entity['text'].lower() for hashtag_entity in tweet['tweet']['entities']['hashtags']]
        hashtag_set |= {*hashtags}

    for hashtag in sorted(list(hashtag_set)):
        print(hashtag)
    print()
