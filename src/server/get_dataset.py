import datetime
import os.path as path
import json
import os

def get_all_datasets_from_file():
    dataset_path=path.dirname(path.dirname(path.abspath(__file__)))+os.sep+"uploaded_datasets"
    dataset_list=os.listdir(dataset_path)
    # check if dataset exists
    if len(dataset_list)==0:
        return {'status': 'No Datasets Found', 'dataset_info':[],'Code':404}
    dataset_info_list=[]
    
    for dataset in dataset_list:
        dataset_info={}
        dataset_info['dataset_id']=dataset
        dataset_info['dataset_size']=os.path.getsize(dataset_path+os.sep+dataset)
        dataset_info['last_modified']=datetime.datetime.fromtimestamp(os.path.getmtime(dataset_path+os.sep+dataset)).strftime('%Y-%m-%d %H:%M:%S')
        dataset_info['number_of_files']=len(os.listdir(dataset_path+os.sep+dataset))
        dataset_info_list.append(dataset_info)
    return {'status': 'Datasets successfully obtained', 'dataset_info':dataset_info_list,'Code':200}

def get_dataset_by_id_from_file(id):
    dataset_path=path.dirname(path.dirname(path.abspath(__file__)))+os.sep+"uploaded_datasets"+os.sep+id
    # check if dataset exists
    if not path.exists(dataset_path):
        return {'status': 'Dataset Not Found', 'dataset_info':[],'Code':404}
    dataset_info={}
    dataset_info['dataset_id']=id
    dataset_info['dataset_size']=os.path.getsize(dataset_path+os.sep)
    dataset_info['last_modified']=datetime.datetime.fromtimestamp(os.path.getmtime(dataset_path)).strftime('%Y-%m-%d %H:%M:%S')
    dataset_info['number_of_files']=len(os.listdir(dataset_path))
    return {'status': 'Dataset successfully obtained', 'dataset_info':dataset_info,'Code':200}