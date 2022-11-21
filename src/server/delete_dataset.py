import json
import os
import os.path as path
import shutil

def delete_dataset_by_id_from_file(id):
    dataset_path=path.dirname(path.dirname(path.abspath(__file__)))+os.sep+"uploaded_datasets"+os.sep+id
    if path.exists(dataset_path):
        shutil.rmtree(dataset_path)
        return {'status': 'Dataset successfully deleted','dataset_id':id,'Code':200}
    else:
        return {'status': 'Dataset Not Found','dataset_id':id,'Code':404}