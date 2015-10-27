#!/usr/bin/python
# -*- coding: utf-8 -*-

import json
import codecs


def dump_json(token_dict, dump_path):
    with open(dump_path, 'w') as output_file:
        json.dump(token_dict, output_file, indent=4)

def dump_unicode(dump_data, dump_path):
    with codecs.open(dump_path, "w", "utf-8-sig") as output_file:
        output_file.write(dump_data)
