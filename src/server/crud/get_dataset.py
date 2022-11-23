import datetime
import os.path as path
import json
import os

def get_dataset_path():
    return path.dirname(path.dirname(path.dirname(path.abspath(__file__))))+os.sep+"uploaded_datasets"

def get_all_datasets_from_file():
    # dataset_path=path.dirname(path.dirname(path.dirname(path.abspath(__file__))))+os.sep+"uploaded_datasets"
    dataset_path=get_dataset_path()
    dataset_list=os.listdir(dataset_path)
    if len(dataset_list)==0:
        return {'status': 'No Datasets Found', 'dataset_info':[],'Code':404}
    dataset_info_list=[]
    
    for dataset in dataset_list:
        dataset_info={}
        dataset_info['dataset_id']=dataset
        dataset_info['dataset_size']=os.path.getsize(dataset_path+os.sep+dataset)
        dataset_info_list.append(dataset_info)
    number_of_datasets=len(dataset_list)
    return {'status': 'Datasets successfully obtained','dataset_count':number_of_datasets ,'dataset_info':dataset_info_list,'Code':200}

def get_dataset_by_id_from_file(id):
    dataset_path=get_dataset_path()+os.sep+id
    if not path.exists(dataset_path):
        return {'status': 'Dataset Not Found', 'dataset_info':[],'Code':404}
    dataset_info={}
    dataset_info['dataset_id']=id
    dataset_info['dataset_size']=os.path.getsize(dataset_path+os.sep)
    dataset_info['last_modified']=datetime.datetime.fromtimestamp(os.path.getmtime(dataset_path)).strftime('%Y-%m-%d %H:%M:%S')
    dataset_info['number_of_files']=len(os.listdir(dataset_path))
    dataset_info['dataset_path']=dataset_path
    dataset_info['dataset_files']=os.listdir(dataset_path)
    return {'status': 'Dataset successfully obtained', 'dataset_info':dataset_info,'Code':200}