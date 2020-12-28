from src.dao.version_dao import VersionDao
from src.models.version_model import VersionModel

default_version = 'v001_data_init'
default_version_dict = {
    'version': default_version
}


def test_version_dao_inserts_record(mongo_db):
    version_model = _build_version_model()
    version_dao = VersionDao(mongo_db)

    version_id = version_dao.insert(version_model)

    # cleanup
    assert version_dao.delete_one(version_model.version)

    assert version_id


def test_version_does_not_find_record(mongo_db):
    version_dao = VersionDao(mongo_db)
    result = version_dao.find_one(default_version)

    assert result is None


def test_version_does_find_record(mongo_db):
    version = _build_version_model()
    version_dao = VersionDao(mongo_db)

    expected_version_id = version_dao.insert(version)

    result_version = version_dao.find_one(default_version)

    # cleanup
    assert version_dao.delete_one(default_version)

    assert expected_version_id == str(result_version._id)


def test_version_dao_delete_no_record(mongo_db):
    version_dao = VersionDao(mongo_db)
    deleted_count = version_dao.delete_one(default_version)
    assert 0 == deleted_count


def test_version_dao_deletes_record(mongo_db):
    version = _build_version_model()
    version_dao = VersionDao(mongo_db)
    version_dao.insert(version)

    deleted_count = version_dao.delete_one(default_version)

    assert 1 == deleted_count


def _build_version_model() -> VersionModel:
    version_model = VersionModel.from_json(default_version_dict)

    return version_model
