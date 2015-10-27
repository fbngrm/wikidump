#!/usr/bin/python


def get_urls(filepath):
    with open(filepath) as f:
        return [x.strip('\n') for x in f.readlines()]
