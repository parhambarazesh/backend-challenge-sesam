from src.server.crud.export_dataset import *
from unittest import mock

@mock.patch('src.server.crud.export_dataset.os.path.exists', return_value=False)
def test_exportdatasettoexcelfromfile_datasetdoesnotexist_returns404(mocker1):
    response=export_dataset_to_excel_from_file('88c9e1b2-0a1b-4567-a886-5c692913cf7d')
    assert response['Code'] == 404

@mock.patch('src.server.crud.export_dataset.os.path.exists', return_value=True)
@mock.patch('src.server.crud.export_dataset.pd.DataFrame.to_excel', return_value=True)
@mock.patch('src.server.crud.export_dataset.pd.concat', return_value=pd.DataFrame(data={'id': [1, 2, 3], 'name': ['a', 'b', 'c']}))
@mock.patch('src.server.crud.export_dataset.os.listdir', return_value=['dataset1','dataset2'])
@mock.patch("builtins.open", new_callable=mock.mock_open)
@mock.patch('src.server.crud.export_dataset.json.load', return_value={'id':1,'name':'test'})
def test_exportdatasettoexcelfromfile_datasetexists_returns200(mocker1, mocker2, mocker3, mocker4, mocker5, mocker6):
    response=export_dataset_to_excel_from_file('88c9e1b2-0a1b-4567-a886-5c692913cf7d')
    assert response['Code'] == 200