from src.server.crud.create_dataset import *
from unittest import mock

@mock.patch('src.server.crud.create_dataset.os.path.exists', return_value=False)
@mock.patch('src.server.crud.create_dataset.json.dump', return_value=True)
def test_createdatasetasfile_datasetnotfound_returns404(mocker1, mocker2):
    response = create_and_save_dataset_as_file([{'a': 1, 'b': 2}, {'c': 3, 'd': 4}])
    assert response['Code'] == 404

@mock.patch('src.server.crud.create_dataset.os.path.exists', return_value=True)
@mock.patch('src.server.crud.create_dataset.json.dump', return_value=True)
@mock.patch("builtins.open", new_callable=mock.mock_open)
@mock.patch('src.server.crud.create_dataset.store_dataset', return_value=True)
def test_createdatasetasfile_datasetfound_returns200(mocker1, mocker2, mocker3, mocker4):
    response = create_and_save_dataset_as_file([{'a': 1, 'b': 2}, {'c': 3, 'd': 4}])
    assert response['Code'] == 200