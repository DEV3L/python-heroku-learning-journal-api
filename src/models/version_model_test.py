from src.models.version_model import VersionModel


def test_version_model_sets_attributes():
    expected_version = 'v001_data_init'

    version_model = VersionModel(expected_version)

    assert expected_version == version_model.version


def test_version_model_returns_json():
    expected_json = {
        'version': 'v001_data_init'
    }

    version_model = VersionModel('v001_data_init')

    assert expected_json == version_model.to_json


def test_version_model_loads_from_json():
    expected_version = 'v001_data_init'

    json_data = {
        'version': expected_version
    }

    version_model = VersionModel.from_json(json_data)

    assert expected_version == version_model.version
