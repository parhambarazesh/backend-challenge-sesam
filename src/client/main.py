import click
import requests
import ast
from src.client.settings import *

@click.group()
def all_commands():
    pass

@click.command()
@click.option('--datasetfile',type=str)
def postdataset(datasetfile):
    if datasetfile:
        with open(datasetfile, 'r') as f:
            dataset = f.read()
        response=requests.post(url, json=ast.literal_eval(dataset))
        click.echo(response.json())

@click.command()
@click.option('--all', is_flag=True)
@click.option('--id', type=str)
def getdatasets(all,id):
    if all:
        response=requests.get(url)
        click.echo(response.json())
    elif id:
        response=requests.get(url+"/"+id)
        click.echo(response.json())

@click.command()
@click.option('--id', type=str)
def deletedataset(id):
    if id:
        response=requests.delete(url+"/"+id)
        click.echo(response.json())

@click.command()
@click.option('--id', type=str)
def exportdataset(id):
    if id:
        response=requests.get(url+"/"+id+'/excel')
        click.echo(response.json())


all_commands.add_command(getdatasets)
all_commands.add_command(postdataset)
all_commands.add_command(deletedataset)
all_commands.add_command(exportdataset)

if __name__ == '__main__':
    all_commands()