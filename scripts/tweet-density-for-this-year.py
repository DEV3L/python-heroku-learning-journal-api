import json
import os
from datetime import datetime
from functools import reduce

from dotenv import load_dotenv

from src.classifiers.hashtags import CLASSIFICATION_ENGINEERING, CLASSIFICATION_AGILE, \
    CLASSIFICATION_LEADERSHIP, CLASSIFICATION_OTHER
from src.extractors.classification_extractor import ClassificationExtractor
from src.extractors.time_extractor import TimeExtractor
from src.models.tweet_event_model import TweetEventModel

load_dotenv()

DATA_SEED_TWITTER_PATH = os.environ.get("DATA_SEED_TWITTER_PATH", "./data/tweet.json")

current_year = str(datetime.today().year)

classifications = {
    CLASSIFICATION_ENGINEERING: 0,
    CLASSIFICATION_AGILE: 0,
    CLASSIFICATION_LEADERSHIP: 0,
    CLASSIFICATION_OTHER: 0
}


def reduce_classifications(result: dict, tweet_event: TweetEventModel) -> dict:
    classification_extractor = ClassificationExtractor(tweet_event)
    classification = classification_extractor.classify()

    result[classification] = result[classification] + 1

    return result


if __name__ == "__main__":
    with open(DATA_SEED_TWITTER_PATH) as data_seed:
        data = json.load(data_seed)

    time_extractor = TimeExtractor(data)
    tweets_from_this_year = time_extractor.tweets_for_year(current_year)

    tweet_hashtags_from_this_year = [
        TweetEventModel([hashtag_entity['text'].lower()
                         for hashtag_entity in tweet['tweet']['entities']['hashtags']], tweet['tweet']['full_text'])
        for tweet in tweets_from_this_year]

    classified_tweets = reduce(reduce_classifications, tweet_hashtags_from_this_year, classifications)

    for key, value in classified_tweets.items():
        print(f'{key}: {value}')
