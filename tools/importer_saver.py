# -*- coding: utf-8 -*-
import json


def from_json(path, filename):
    if '.json' in filename:
        filename = filename.replace('.json', '')
    with open(f'{path}/{filename}.json') as f:
        data = json.load(f)
    return data
    