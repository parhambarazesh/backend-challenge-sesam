import json
import os
import os.path as path
import pandas as pd

def get_dataset_path():
    return path.dirname(path.dirname(path.dirname(path.abspath(__file__))))+os.sep+"uploaded_datasets"

def get_exported_dataset_path():
    return path.dirname(path.dirname(path.dirname(path.abspath(__file__))))+os.sep+"exported_datasets"

def export_dataset_to_excel_from_file(id):
    dataset_path=get_dataset_path()+os.sep+id
    path_to_save=get_exported_dataset_path()+os.sep+id+".xlsx"
    if path.exists(dataset_path):
        files=os.listdir(dataset_path)
        df=pd.DataFrame()
        for file in files:
            with open(dataset_path+os.sep+file) as f:
                data=json.load(f)
            
            df=pd.concat([df,pd.DataFrame.from_dict(data,orient='index').T])
        df=df.sort_values(by=['id'])
        df.to_excel(path_to_save,index=False)
        return {'status': 'Dataset successfully exported to excel','dataset_id':id,'Code':200}
    else:
        return {'status': 'Dataset Not Found','dataset_id':id,'Code':404}
