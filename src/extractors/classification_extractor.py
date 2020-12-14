from src.classifiers.hashtags import CLASSIFICATION_OTHER, CLASSIFICATION_AGILE, CLASSIFIED_HASHTAGS, \
    CLASSIFICATION_ENGINEERING, CLASSIFICATION_LEADERSHIP
from src.models.tweet_event_model import TweetEventModel


class ClassificationExtractor:
    CLASSIFICATIONS = [
        CLASSIFICATION_AGILE,
        CLASSIFICATION_ENGINEERING,
        CLASSIFICATION_OTHER,
        CLASSIFICATION_LEADERSHIP
    ]

    tweet_event = None

    def __init__(self, tweet_event: TweetEventModel):
        self.tweet_event = tweet_event

    def classify(self) -> int:
        tag_classifications = {
            classification: self._classify_tag(classification)
            for classification in self.CLASSIFICATIONS
        }

        is_all_zeros = not sum(tag_classifications.values())
        if is_all_zeros:
            return CLASSIFICATION_OTHER

        classification = max(tag_classifications, key=tag_classifications.get)
        return classification

    def _classify_tag(self, classification: str):
        return len(list(filter(
            lambda hashtag: classification == CLASSIFIED_HASHTAGS.get(hashtag), self.tweet_event.hashtags)))
