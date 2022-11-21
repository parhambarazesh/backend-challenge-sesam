import sys
import os.path as path
sys.path.append(path.dirname(path.dirname(path.dirname(path.abspath(__file__)))))
from flask import Flask, render_template, request, redirect, url_for, flash, jsonify
from src.server.create_dataset import *
from src.server.get_dataset import *

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
        delete_dataset_by_id_from_file(dataset_id)
        return {'status': 'Dataset successfully deleted','Code':200}
if __name__ == '__main__':
    app.run()