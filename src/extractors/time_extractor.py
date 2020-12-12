from typing import List, Dict


class TimeExtractor:
    tweet_data = None

    def __init__(self, tweet_data: List[Dict]):
        self.tweet_data = tweet_data

    def tweets_for_year(self, year: str) -> List[Dict]:
        if not self.tweet_data:
            return []

        tweets_for_year = []

        for tweet in self.tweet_data:
            created_at = tweet['tweet']['created_at']

            if year in created_at:
                tweets_for_year.append(tweet)

        return tweets_for_year
