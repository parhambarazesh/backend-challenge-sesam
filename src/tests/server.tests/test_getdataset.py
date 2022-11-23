from src.server.crud.get_dataset import *
from unittest import mock

@mock.patch('src.server.crud.get_dataset.os.listdir', return_value=[])
def test_getalldatasetsfromfile_nodatabasefound_returns404(mocker1):
    response = get_all_datasets_from_file()
    assert response['Code'] == 404

@mock.patch('src.server.crud.get_dataset.os.listdir', return_value=['dataset1', 'dataset2'])
@mock.patch('src.server.crud.get_dataset.os.path.getsize', return_value=4096)
def test_getalldatasetsfromfile_databasefound_returns200(mocker1, mocker2):
    response = get_all_datasets_from_file()
    assert response['Code'] == 200

@mock.patch('src.server.crud.get_dataset.os.path.exists', return_value=False)
def test_getdatasetbyidfromfile_datasetnotfound_returns404(mocker1):
    response = get_dataset_by_id_from_file('88c9e1b2-0a1b-4567-a886-5c692913cf7d')
    assert response['Code'] == 404

@mock.patch('src.server.crud.get_dataset.os.path.exists', return_value=True)
@mock.patch('src.server.crud.get_dataset.os.path.getsize', return_value=4096)
@mock.patch('src.server.crud.get_dataset.os.path.getmtime', return_value=0)
@mock.patch('src.server.crud.get_dataset.os.listdir', return_value=['file1', 'file2'])
def test_getdatasetbyidfromfile_datasetfound_returns200(mocker1, mocker2, mocker3, mocker4):
    response = get_dataset_by_id_from_file('88c9e1b2-0a1b-4567-a886-5c692913cf7d')
    assert response['Code'] == 200