from typing import Dict


class VersionModel:
    def __init__(self, version: str = None):
        self.version = version

    @property
    def to_json(self) -> Dict:
        return vars(self)

    @staticmethod
    def from_json(json_data: Dict):
        version_model = VersionModel()
        version_model.__dict__.update(**json_data)

        return version_model
