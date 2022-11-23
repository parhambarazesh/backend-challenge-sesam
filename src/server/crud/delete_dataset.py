import json
import os
import os.path as path
import shutil
from src.db_connector.mongodb import delete_dataset

def get_dataset_path():
    return path.dirname(path.dirname(path.dirname(path.abspath(__file__))))+os.sep+"uploaded_datasets"

def delete_dataset_by_id_from_file(id):
    dataset_path=get_dataset_path()+os.sep+id
    if path.exists(dataset_path):
        shutil.rmtree(dataset_path)
        delete_dataset(id)
        return {'status': 'Dataset successfully deleted','dataset_id':id,'Code':200}
    else:
        return {'status': 'Dataset Not Found','dataset_id':id,'Code':404}