import json
import os
import os.path as path
from uuid import uuid4

from src.db_connector.mongodb import store_dataset

def get_dataset_path():
    return path.dirname(path.dirname(path.dirname(path.abspath(__file__))))+os.sep+"uploaded_datasets"

def create_and_save_dataset_as_file(json_list):
    try:
        dataset_id=str(uuid4())
        dataset_path=get_dataset_path()+os.sep+dataset_id
        if not path.exists(dataset_path):
            os.makedirs(dataset_path)
        object_id_list=[]
        for dict_data in json_list:
            object_id=str(uuid4())
            file_name=dataset_path+os.sep+object_id+".json"
            with open(file_name, 'w') as outfile:
                json.dump(dict_data, outfile, indent=4)
                store_dataset(dataset_id,dict_data)
            object_id_list.append(object_id)
        return {'status': 'Dataset successfully created', 'dataset_id':dataset_id, 'object_ids':object_id_list,'Code':200}
    except Exception as e:
        return {'status': 'Dataset Not Created', 'dataset_info':[],'Code':404, 'error':str(e)}