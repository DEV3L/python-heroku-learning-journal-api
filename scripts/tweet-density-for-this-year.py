import json
import os
from datetime import datetime
from functools import reduce
from typing import List

from dotenv import load_dotenv

from src.classifiers.hashtags import CLASSIFICATION_ENGINEERING, CLASSIFICATION_AGILE, \
    CLASSIFICATION_LEADERSHIP, CLASSIFICATION_OTHER, classified_hashtags
from src.extractors.time_extractor import TimeExtractor

load_dotenv()

DATA_SEED_TWITTER_PATH = os.environ.get("DATA_SEED_TWITTER_PATH", "./data/tweet.json")

current_year = str(datetime.today().year)

classifications = {
    CLASSIFICATION_ENGINEERING: 0,
    CLASSIFICATION_AGILE: 0,
    CLASSIFICATION_LEADERSHIP: 0,
    CLASSIFICATION_OTHER: 0
}


def classify(classification: str, tweet_hashtags_to_classify: List[str]) -> int:
    return len(list(filter(
        lambda hashtag: classification == classified_hashtags.get(hashtag), tweet_hashtags_to_classify)))


def reduce_classifications(result: dict, tweet_hashtags: list) -> dict:
    classification_keys = result.keys()

    tag_classifications = {
        classification: classify(classification, tweet_hashtags)
        for classification in classification_keys
    }

    classification = max(tag_classifications, key=tag_classifications.get)
    result[classification] = result[classification] + 1

    return result


if __name__ == "__main__":
    with open(DATA_SEED_TWITTER_PATH) as data_seed:
        data = json.load(data_seed)

    time_extractor = TimeExtractor(data)
    tweets_from_this_year = time_extractor.tweets_for_year(current_year)

    tweet_hashtags_from_this_year = [
        [hashtag_entity['text'].lower()
         for hashtag_entity in tweet['tweet']['entities']['hashtags']]
        for tweet in tweets_from_this_year]

    classified_tweets = reduce(reduce_classifications, tweet_hashtags_from_this_year, classifications)

    for key, value in classified_tweets.items():
        print(f'{key}: {value}')
