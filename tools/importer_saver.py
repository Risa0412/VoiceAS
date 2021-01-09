# -*- coding: utf-8 -*-
import json


def from_json(path, filename):
    if '.json' in filename:
        filename = filename.replace('.json', '')
    with open(f'{path}/{filename}.json') as f:
        data = json.load(f)
    return data
    
def from_txt(path, filename):
    if '.txt' in filename:
        filename = filename.replace('.txt', '')
    with open(f'{path}/{filename}.txt', mode='r', encoding='utf-8') as f:
        data = f.read()
    return data
