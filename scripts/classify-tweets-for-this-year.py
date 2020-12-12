import json
import os
from datetime import datetime
from functools import reduce

from dateutil.parser import parse
from dotenv import load_dotenv

load_dotenv()

DATA_SEED_TWITTER_PATH = os.environ.get("DATA_SEED_TWITTER_PATH", "./data/tweet.json")

current_year = datetime.today().year
first_of_year = parse(f'Jan 1 00:00:00 +0000 {current_year}')
end_of_year = parse(f'Dec 31 23:59:59 +0000 {current_year}')


def filter_by_this_year(tweet: dict) -> bool:
    created_at = parse(tweet['tweet']['created_at'])
    return first_of_year <= created_at <= end_of_year


def filter_by_audiobook_start(tweet: dict) -> bool:
    text = tweet['tweet']['full_text']
    return "Started listening to:" in text or "Finished listening to:" in text


def reduce_book_titles(result: set, tweet: dict) -> set:
    text = tweet['tweet']['full_text']
    title = text.split(":")[1].split("\n")[0].strip()
    result.add(title)
    return result


if __name__ == "__main__":
    with open(DATA_SEED_TWITTER_PATH) as data_seed:
        data = json.load(data_seed)

    tweets_from_this_year = list(filter(filter_by_this_year, data))
    audio_books_from_this_year = list(filter(filter_by_audiobook_start, tweets_from_this_year))

    audio_book_titles = list(reduce(reduce_book_titles, audio_books_from_this_year, set()))

    print(f'## {current_year} Audiobooks:')
    for book_title in audio_book_titles:
        print(f'- {book_title}')
