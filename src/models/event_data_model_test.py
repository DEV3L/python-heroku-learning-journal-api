from src.models.event_data_model import EventDataModel


def test_event_data_model_sets_attributes():
    expected_source = 'twitter'
    expected_data = {'key': 'value'}

    event_data_model = EventDataModel(expected_source, expected_data)

    assert expected_source == event_data_model.source
    assert expected_data == event_data_model.data


def test_event_data_model_returns_json():
    expected_json = {
        'author': None,
        'classification': None,
        'data': {'key': 'value'},
        'images': [],
        'kcv': None,
        'medium': None,
        'raw_text': None,
        'source': 'twitter',
        'source_id': None,
        'tags': [],
        'text': None,
        'user': None,
        'version': 0,
    }

    event_data_model = EventDataModel('twitter', {'key': 'value'})

    assert expected_json == event_data_model.to_json
