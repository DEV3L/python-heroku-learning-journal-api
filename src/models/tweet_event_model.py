from typing import List

DEFAULT_KCV_VALUE = 2


class TweetEventModel:
    hashtags = None
    text = None
    kcv = None

    def __init__(self, hashtags: List[str], text: str):
        self.hashtags = hashtags
        self.text = text
        self.kcv = DEFAULT_KCV_VALUE
