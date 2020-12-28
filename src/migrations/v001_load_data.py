import json
import os

from src.dao.event_data_dao import EventDataDao
from src.dao.mongodb import MongoDb
from src.dao.version_dao import VersionDao
from src.models.event_data_model import EventDataModel
from src.models.version_model import VersionModel

DATA_SEED_TWITTER_PATH = os.environ.get('DATA_SEED_TWITTER_PATH', './data/tweet.json')


class V001LoadData:
    version = "V001_Load_Data"

    def run(self):
        mongo_db = MongoDb.instance()
        version_dao = VersionDao(mongo_db)

        if version_dao.find_one(self.version):
            return

        version_model = VersionModel(self.version)
        version_dao.insert(version_model)

        with open(DATA_SEED_TWITTER_PATH) as data_seed:
            data = json.load(data_seed)

        event_data_dao = EventDataDao(mongo_db)

        for event_data in data:
            event_data_model = EventDataModel("twitter", event_data)
            event_data_dao.insert(event_data_model)
