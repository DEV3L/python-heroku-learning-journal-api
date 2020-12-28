from datetime import datetime

from pymongo.database import Database

from src.models.version_model import VersionModel


class VersionDao:
    def __init__(self, db: Database):
        self.version_collection = db['version']

    def insert(self, version_model: VersionModel) -> str:
        values = {**version_model.to_json, 'updated': datetime.utcnow()}
        insert_result = self.version_collection.insert_one(values)
        return str(insert_result.inserted_id)

    def find_one(self, version: str) -> VersionModel:
        query = {'version': version}
        result = self.version_collection.find_one(query)
        if result is None:
            return None

        version_model = VersionModel.from_json(result)
        return version_model

    def delete_one(self, version: str) -> int:
        query = {'version': version}
        return self.version_collection.delete_one(query).deleted_count
