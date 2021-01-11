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


def test_event_data_dao_does_not_update_record_with_invalid_identifier(mongo_db):
    # event_data_model = _build_event_data_model()
    # event_data_dao = EventDataDao(mongo_db)
    #
    # result = event_data_dao.update(event_data_model)
    #
    # assert not result
    pass


#
#
# def test_event_data_dao_does_update_record(mongo_db):
#     pass
#
#
# def test_event_data_dao_does_not_find_record(mongo_db):
#     version_dao = VersionDao(mongo_db)
#     result = version_dao.find_one(default_version)
#
#     assert result is None
#
#
# def test_event_data_dao_does_find_one_record(mongo_db):
#     version = _build_version_model()
#     version_dao = VersionDao(mongo_db)
#
#     expected_version_id = version_dao.insert(version)
#
#     result_version = version_dao.find_one(default_version)
#
#     # cleanup
#     assert version_dao.delete_one(default_version)
#
#     assert expected_version_id == str(result_version._id)
#
#
# def test_event_data_dao_does_find_multiple_records(mongo_db):
#     version = _build_version_model()
#     version_dao = VersionDao(mongo_db)
#
#     expected_version_id = version_dao.insert(version)
#
#     result_version = version_dao.find_one(default_version)
#
#     # cleanup
#     assert version_dao.delete_one(default_version)
#
#     assert expected_version_id == str(result_version._id)
#
#
# def test_event_data_dao_delete_no_record(mongo_db):
#     version_dao = VersionDao(mongo_db)
#     deleted_count = version_dao.delete_one(default_version)
#     assert 0 == deleted_count
#
#
# def test_event_data_dao_deletes_record(mongo_db):
#     version = _build_version_model()
#     version_dao = VersionDao(mongo_db)
#     version_dao.insert(version)
#
#     deleted_count = version_dao.delete_one(default_version)
#
#     assert 1 == deleted_count
#

def _build_event_data_model():
    return EventDataModel(source, data)
