import json
import os

from dotenv import load_dotenv

load_dotenv()

DATA_SEED_TWITTER_PATH = os.environ.get("DATA_SEED_TWITTER_PATH", "./data/tweet.json")

if __name__ == "__main__":
    with open(DATA_SEED_TWITTER_PATH) as data_seed:
        data = json.load(data_seed)

    tweets_text = [tweet['tweet']['full_text']
                   [int(tweet['tweet']['display_text_range'][0]): int(tweet['tweet']['display_text_range'][1])]
                   for tweet in data]

    tweets_with_mediums = list(filter(lambda text: ":" in text.split("\n")[0].replace("https:", "")
                                                   and len(text.split("\n")) > 2
                                                   and not text.startswith("RT @"), tweets_text))

    mediums_set = {tweet_text.split("\n")[0].split(":")[0].lower() for tweet_text in tweets_with_mediums}
    mediums = sorted(list(mediums_set))

"""
attended : conference/session
attending : conference/session
i'm at : conference/session
lightning talk : conference/session

watched : video

began: course
completed: course

started listening to : audiobook start
finished listening : audiobook end

started reading : book start
finished reading : book end

listend to : podcast
listened to : podcast

presented : speaking
"""
