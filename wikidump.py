#!/usr/bin/python
# -*- coding: utf-8 -*-

from wiki_client import WikiClient
import parser
import reader
import dump
import traceback
import sys
import os

ROOT_URL = 'https://en.wikipedia.org'


class WikiDump(object):

    def __init__(self, args, urls, wikiclient):
        self._args = args
        self._urls = urls
        self._wikiclient = wikiclient

    def run(self, depth=0, urls=None):
        urls = urls or self._urls
        # Dump
        for url in urls:
            # Ensure url is an instance of str
            if isinstance(url, unicode):
                url = url.encode('utf-8')

            self._dump(url)

            # Recursion
            if depth:
                links = [ROOT_URL + link['href']
                    for link in self._wikiclient.links]
                self.run(depth-1, links)

    def _dump(self, url):
        try:
            self._wikiclient.dump(url)

            if self._args.get('verbose'):
                self._print()

            if args.get('dump'):
                self._export(url)

        except Exception:
            print 'failed to dump data'
            traceback.print_exc()
            sys.exit()

    def _print(self):
        if self._args.get('text'):
            print(self._wikiclient.text)

        if self._args.get('links'):
            print(self._wikiclient.links)

        if self._args.get('paragraphs'):
            print(self._wikiclient.paragraphs)

    def _export(self, url):
            # Get the filename from url
            filename = url.split('/')[-1]
            dump_path = os.path.abspath(
                os.path.join(args.get('dump'), filename))
            dump_data = dict()

            if self._args.get('text'):
                dump_data['text'] = self._wikiclient.text

            if self._args.get('links'):
                dump_data['links'] = self._wikiclient.links

            if self._args.get('paragraphs'):
                dump_data['paragraphs'] = self._wikiclient.paragraphs

            dump.dump_json(dump_data, dump_path + '.json')

            if self._args.get('text'):
                text = dump_data['text']
                if isinstance(text, str):
                    text = text.decode('utf-8')
                dump.dump_unicode(text, dump_path + '.txt')


if __name__ == '__main__':
    # Get the cmd-line args
    args = parser.parse()

    # Get the url[s]
    if args.get('url'):
        urls = [args.get('url')]
    elif args.get('url_file'):
        try:
            urls = reader.get_urls(args.get('url_file'))
        except Exception as e:
            print 'failed to read urls'
            traceback.print_exc()
            sys.exit()
    else:
        print 'need url'
        sys.exit()

    try:
        depth = int(args.get('recursion_depth'))
    except:
        depth = 0
    wikidump = WikiDump(args, urls, WikiClient())
    wikidump.run(depth)
