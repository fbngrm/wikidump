#!/usr/bin/python

import json


def dump_json(token_dict, dump_path):
    with open(dump_path, 'w') as output_file:
        json.dump(token_dict, output_file, indent=4)
