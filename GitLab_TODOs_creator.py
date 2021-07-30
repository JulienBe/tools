import click
import re
import requests
import os

from sys import argv

assignee_id=21
headers = {
    'PRIVATE-TOKEN': 'xxxxxx',
    'Content-Type': 'application/json',
}

file=argv[1]
todos=[]
filename=os.path.basename(file)
title=f'TODOs on {filename}'

print(f'Parsing file {filename}')
with open(file, 'r') as f:
    for line in f.readlines():
        if 'TODO' in line:
            todo=re.sub(' +', ' ', line)
            todo=re.sub(' // TODO : ', '', todo)
            todo=re.sub(' // TODO :', '', todo)
            todo=re.sub(' // TODO ', '', todo)
            todo=re.sub(' // TODO: ', '', todo)
            todo=re.sub(' // TODO:', '', todo)
            todo=re.sub(' // TODO', '', todo)
            todo=f'- [ ] {todo}'
            print(f'Adding todo: {todo}')
            todos.append(todo)

if not todos:
    print("Could not find any TODO! The syntax in 'TODO'")
    exit(1)

if click.confirm('Do you want to continue?', default=True):  
    payload = {'title':title,'labels':'Engine','assignee_id':assignee_id,'description':' '.join(str(todo)+'\n' for todo in todos)}
    response = requests.post('https://gitlab.entreprise.com/api/v4/projects/117/issues', headers=headers, json=payload, verify=False)
    print(f'response: {response}')
    print(f'response code: {response.status_code}')
