import os
import click
import json
import requests
import ast
from src.client.settings import *
from src.client.secrets import *
import urllib3
urllib3.disable_warnings(urllib3.exceptions.SecurityWarning)

def get_cert():
    return os.path.dirname(os.path.abspath(__file__))+os.sep+"secrets"+os.sep+"cert.pem"

@click.group()
def all_commands():
    pass

@click.command()
@click.option('--datasetfile',type=str,help='dataset file url')
def postdataset(datasetfile):
    if datasetfile:
        with open(datasetfile, 'r') as f:
            dataset = f.read()
        response=requests.post(url, json=ast.literal_eval(dataset), verify=get_cert())
        click.echo(json.dumps(response.json(), indent=4))

@click.command()
@click.option('--all', is_flag=True, help='obtains all datasets')
@click.option('--id', type=str, help='id of the dataset to obtain')
def getdataset(all,id):
    if all:
        response=requests.get(url,verify=get_cert())
        click.echo(json.dumps(response.json(), indent=4))
    elif id:
        response=requests.get(url+"/"+id,verify=get_cert())
        click.echo(json.dumps(response.json(), indent=4))

@click.command()
@click.option('--id', type=str, help='id of dataset to delete')
def deletedataset(id):
    if id:
        response=requests.delete(url+"/"+id,verify=get_cert())
        click.echo(json.dumps(response.json(), indent=4))

@click.command()
@click.option('--id', type=str, help='id of dataset to export')
def exportdataset(id):
    if id:
        response=requests.get(url+"/"+id+'/excel',verify=get_cert())
        click.echo(json.dumps(response.json(), indent=4))


all_commands.add_command(getdataset)
all_commands.add_command(postdataset)
all_commands.add_command(deletedataset)
all_commands.add_command(exportdataset)

if __name__ == '__main__':
    all_commands()