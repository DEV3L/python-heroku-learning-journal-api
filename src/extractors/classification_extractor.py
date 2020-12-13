from src.classifiers.hashtags import CLASSIFICATION_OTHER, CLASSIFICATION_AGILE
from src.models.tweet_event_model import TweetEventModel


class ClassificationExtractor:
    tweet_event = None

    def __init__(self, tweet_event: TweetEventModel):
        self.tweet_event = tweet_event

    def classify(self):
        if CLASSIFICATION_AGILE in self.tweet_event.hashtags:
            return CLASSIFICATION_AGILE
        return CLASSIFICATION_OTHER
