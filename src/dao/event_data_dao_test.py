from src.dao.event_data_dao import EventDataDao

from src.models.event_data_model import EventDataModel

source = 'twitter'
data = {
    'key': 'value'
}

default_weapon_event_dict = {
    'source': source,
    'data': data
}


def test_event_data_dao_inserts_record(mongo_db):
    event_data_model = _build_event_data_model()
    event_data_dao = EventDataDao(mongo_db)

    event_data_id = event_data_dao.insert(event_data_model)

    assert event_data_id


def _build_event_data_model():
    return EventDataModel(source, data)
