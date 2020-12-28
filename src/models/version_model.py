from typing import Dict


class VersionModel:
    def __init__(self, version: str):
        self.version = version

    @property
    def to_json(self) -> Dict:
        return vars(self)
