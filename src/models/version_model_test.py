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
