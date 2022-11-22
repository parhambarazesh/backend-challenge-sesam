import sys
import os.path as path
sys.path.append(path.dirname(path.dirname(path.dirname(path.abspath(__file__)))))
from flask import Flask, request
from src.server.create_dataset import *
from src.server.get_dataset import *
from src.server.delete_dataset import *
from src.server.export_dataset import *

app=Flask(__name__)

@app.route('/')
def home():
    return {'message': 'Hello World'}

@app.route('/datasets', methods=['POST'])
def post_dataset():
    if request.method == 'POST':
        response=create_and_save_dataset_as_file(request.json)
        return response

@app.route('/datasets', methods=['GET'])
def get_dataset():
    if request.method == 'GET':
        response=get_all_datasets_from_file()
        return response

@app.route('/datasets/<dataset_id>', methods=['GET'])
def get_dataset_by_id(dataset_id):
    if request.method == 'GET':
        response=get_dataset_by_id_from_file(dataset_id)
        return response

@app.route('/datasets/<dataset_id>', methods=['DELETE'])
def delete_dataset_by_id(dataset_id):
    if request.method == 'DELETE':
        response=delete_dataset_by_id_from_file(dataset_id)
        return response

@app.route('/datasets/<dataset_id>/excel', methods=['GET'])
def export_dataset_to_excel(dataset_id):
    if request.method == 'GET':
        response=export_dataset_to_excel_from_file(dataset_id)
        return response
        
if __name__ == '__main__':
    current_dir = path.dirname(path.abspath(__file__))
    if not path.exists(path.dirname(path.dirname(path.abspath(__file__)))+os.sep+"uploaded_datasets"):
        os.mkdir(path.dirname(path.dirname(path.abspath(__file__)))+os.sep+"uploaded_datasets")
    if not path.exists(path.dirname(path.dirname(path.abspath(__file__)))+os.sep+"exported_datasets"):
        os.mkdir(path.dirname(path.dirname(path.abspath(__file__)))+os.sep+"exported_datasets")
    app.run(host='0.0.0.0', port=5000,ssl_context=(f'{current_dir}/secrets/cert.pem', f'{current_dir}/secrets/key.pem'))