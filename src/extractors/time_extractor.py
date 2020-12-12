from typing import List, Dict

from dateutil.parser import parse

FIRST_OF_YEAR = "Jan 1 00:00:00 +0000 "
END_OF_YEAR = "Dec 31 23:59:59 +0000 "


class TimeExtractor:
    tweet_data = None

    def __init__(self, tweet_data: List[Dict]):
        self.tweet_data = tweet_data

        self._year = None
        self._first_of_year = None
        self._end_of_year = None

    def tweets_for_year(self, year: str) -> List[Dict]:
        if not self.tweet_data:
            return []

        self._year = year
        self._first_of_year = parse(f'{FIRST_OF_YEAR}{year}')
        self._end_of_year = parse(f'{END_OF_YEAR}{year}')

        return list(filter(self._filter_by_year, self.tweet_data))

    def _filter_by_year(self, tweet: dict) -> bool:
        created_at = parse(tweet['tweet']['created_at'])
        return self._first_of_year <= created_at <= self._end_of_year
