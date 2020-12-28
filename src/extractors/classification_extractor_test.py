from src.classifiers.hashtags import CLASSIFICATION_OTHER, CLASSIFICATION_AGILE, CLASSIFICATION_ENGINEERING
from src.extractors.classification_extractor import ClassificationExtractor
from src.models.tweet_event_model import TweetEventModel


def test_extract_tweets_for_classification_zero():
    expected_classification = CLASSIFICATION_OTHER
    tweet_event = TweetEventModel([], '')

    classification_extractor = ClassificationExtractor(tweet_event)
    classification = classification_extractor.classify()

    assert expected_classification == classification


def test_extract_tweets_for_agile():
    expected_classification = CLASSIFICATION_AGILE
    tweet_event = TweetEventModel(['agile'], '')

    classification_extractor = ClassificationExtractor(tweet_event)
    classification = classification_extractor.classify()

    assert expected_classification == classification


def test_extract_tweets_for_engineering():
    expected_classification = CLASSIFICATION_ENGINEERING
    tweet_event = TweetEventModel(['engineering'], '')

    classification_extractor = ClassificationExtractor(tweet_event)
    classification = classification_extractor.classify()

    assert expected_classification == classification


def test_extract_tweets_for_agile_not_found():
    expected_classification = CLASSIFICATION_OTHER
    tweet_event = TweetEventModel(['agle'], '')

    classification_extractor = ClassificationExtractor(tweet_event)
    classification = classification_extractor.classify()

    assert expected_classification == classification


def test_extract_tweets_for_agile_many():
    expected_classification = CLASSIFICATION_AGILE
    tweet_event = TweetEventModel(['agile', 'lean', 'engineering'], '')

    classification_extractor = ClassificationExtractor(tweet_event)
    classification = classification_extractor.classify()

    assert expected_classification == classification
