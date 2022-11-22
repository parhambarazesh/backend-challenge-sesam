import pymongo
from src.db_connector.settings import *

def connect_to_db(dataset_id):
    try:
        client = pymongo.MongoClient(db_url)
        db = client[db_name]
        collection = db[dataset_id]
        return collection
    except Exception as e:
        return {'message': f'Error while connecting to database: {e}'}

def store_dataset(dataset_id,json_data):
    try:
        collection=connect_to_db(dataset_id)
        collection.insert_one(json_data)
        return {'message': 'Data inserted successfully'}
    except Exception as e:
        return {'message': f'Error while inserting data into database: {e}'}

def delete_dataset(dataset_id):
    try:
        collection=connect_to_db(dataset_id)
        collection.drop()
        return {'message': 'Data deleted successfully'}
    except Exception as e:
        return {'message': f'Error while deleting data from database: {e}'}