from src.classifiers.hashtags import CLASSIFICATION_OTHER, CLASSIFICATION_AGILE
from src.extractors.classification_extractor import ClassificationExtractor
from src.models.tweet_event_model import TweetEventModel

tweet_engineering = {
    'tweet':
        {
            'hashtags': ['engineering'],
        }
}

tweet_agile = {
    'tweet':
        {
            'hashtags': ['agile'],
        }
}

tweet_multiple_agile = {
    'tweet':
        {
            'hashtags': ['agile', 'lean', 'engineering'],
        }
}


def test_extract_tweets_for_classification_zero():
    expected_classification = CLASSIFICATION_OTHER
    tweet_event = TweetEventModel([], "")

    classification_extractor = ClassificationExtractor(tweet_event)
    classification = classification_extractor.classify()

    assert expected_classification == classification


def test_extract_tweets_for_agile():
    expected_classification = CLASSIFICATION_AGILE
    tweet_event = TweetEventModel(["agile"], "")

    classification_extractor = ClassificationExtractor(tweet_event)
    classification = classification_extractor.classify()

    assert expected_classification == classification


def test_extract_tweets_for_agile_not_found():
    expected_classification = CLASSIFICATION_OTHER
    tweet_event = TweetEventModel(["agle"], "")

    classification_extractor = ClassificationExtractor(tweet_event)
    classification = classification_extractor.classify()

    assert expected_classification == classification

#
# def test_extract_tweets_for_year_many():
#     expected_count = 1
#     tweet_data = [tweet_2019, tweet_2020]
#
#     time_extractor = TimeExtractor(tweet_data)
#
#     tweets_for_year = time_extractor.tweets_for_year("2020")
#
#     assert expected_count == len(tweets_for_year)
