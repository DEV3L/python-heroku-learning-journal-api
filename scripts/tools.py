import json
import os
from typing import Dict, List
from datetime import datetime
from dotenv import load_dotenv

from src.extractors.time_extractor import TimeExtractor

load_dotenv()

year_offset = 1
year = str(datetime.today().year - year_offset)

DATA_SEED_TWITTER_PATH = os.environ.get('DATA_SEED_TWITTER_PATH', './data/tweet.json')


def load_seed_data() -> List[Dict]:
    with open(DATA_SEED_TWITTER_PATH) as data_seed:
        return json.load(data_seed)


def load_year_data() -> List[Dict]:
    data = load_seed_data()

    time_extractor = TimeExtractor(data)
    return time_extractor.tweets_for_year(year)


def filter_classifiers(tweet: dict, classifiers: list) -> bool:
    text = tweet['tweet']['full_text']
    lower_text = text.lower()

    is_found = False
    for classifier in classifiers:
        is_found = is_found or classifier in lower_text

    return is_found


def reduce_titles(result: set, tweet: dict) -> set:
    text = tweet['tweet']['full_text']
    title = text.split(':')[1].split('\n')[0].strip()
    result.add(title)
    return result
