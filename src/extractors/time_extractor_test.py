from src.extractors.time_extractor import TimeExtractor

tweet_2020 = {
    'tweet':
        {
            'created_at': 'Thu Jan 09 20:23:34 +0000 2020',
        }
}

tweet_2019 = {
    'tweet':
        {
            'created_at': 'Thu Jan 09 20:23:34 +0000 2019',
        }
}


def test_extract_tweets_for_year_zero():
    tweet_data = []

    time_extractor = TimeExtractor(tweet_data)

    tweets_for_year = time_extractor.tweets_for_year('2020')

    assert not tweets_for_year


def test_extract_tweets_for_year_one():
    expected_count = 1
    tweet_data = [tweet_2020]

    time_extractor = TimeExtractor(tweet_data)

    tweets_for_year = time_extractor.tweets_for_year('2020')

    assert expected_count == len(tweets_for_year)


def test_extract_tweets_for_year_not_found():
    expected_count = 0
    tweet_data = [tweet_2020]

    time_extractor = TimeExtractor(tweet_data)

    tweets_for_year = time_extractor.tweets_for_year('2019')

    assert expected_count == len(tweets_for_year)


def test_extract_tweets_for_year_many():
    expected_count = 1
    tweet_data = [tweet_2019, tweet_2020]

    time_extractor = TimeExtractor(tweet_data)

    tweets_for_year = time_extractor.tweets_for_year('2020')

    assert expected_count == len(tweets_for_year)
