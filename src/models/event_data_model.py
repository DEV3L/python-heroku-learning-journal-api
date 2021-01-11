from typing import Dict


class EventDataModel:
    def __init__(self, source: str, data: Dict, source_id: str = None, version: int = 0):
        self.source = source
        self.source_id = source_id
        self.version = version
        self.data = data

        self.user = None

        self.tags = []
        self.images = []

        self.author = None

        self.raw_text = None
        self.text = None
        self.medium = None
        self.classification = None
        self.kcv = None

    @property
    def to_json(self) -> Dict:
        return vars(self)
