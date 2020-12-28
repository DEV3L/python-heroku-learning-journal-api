from datetime import datetime

from pymongo.database import Database

from src.models.event_data_model import EventDataModel


class EventDataDao:
    def __init__(self, db: Database):
        self.event_data_collection = db['event_data']

    def insert(self, event_data_model: EventDataModel) -> str:
        values = {**event_data_model.to_json, 'updated': datetime.utcnow()}
        insert_result = self.event_data_collection.insert_one(values)
        return str(insert_result.inserted_id)
