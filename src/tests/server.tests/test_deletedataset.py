from src.server.crud.delete_dataset import *
from unittest import mock

@mock.patch('src.server.crud.delete_dataset.os.path.exists', return_value=False)
def test_deletedatasetbyidfromfile_datasetdoesnotexist_returns404(mocker1):
    response=delete_dataset_by_id_from_file('88c9e1b2-0a1b-4567-a886-5c692913cf7d')
    assert response['Code'] == 404

@mock.patch('src.server.crud.delete_dataset.os.path.exists', return_value=True)
@mock.patch('src.server.crud.delete_dataset.shutil.rmtree', return_value=True)
@mock.patch('src.server.crud.delete_dataset.delete_dataset', return_value=True)
def test_deletedatasetbyidfromfile_datasetexists_returns200(mocker1, mocker2, mocker3):
    response=delete_dataset_by_id_from_file('88c9e1b2-0a1b-4567-a886-5c692913cf7d')
    assert response['Code'] == 200
