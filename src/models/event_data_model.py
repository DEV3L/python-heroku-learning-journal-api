from typing import Dict


class EventDataModel:
    def __init__(self, source: str, data: Dict):
        self.source = source
        self.data = data

    @property
    def to_json(self) -> Dict:
        return vars(self)
