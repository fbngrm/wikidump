#!/usr/bin/python
# -*- coding: utf-8 -*-

from wiki_client import WikiClient
import parser
import reader
import traceback
import sys

# Get the cmd-line args
args = parser.parse()

# Get the url[s]
if args.get('u'):
    urls = list(args.get('url'))
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

# Init wikiclient
wikidump = WikiClient(urls[0])

# Dump
for url in urls:

    # Ensure url is an instance of str
    if isinstance(url, unicode):
        url = url.encode('utf-8')

    if args.get('dump'):
        # Get the filename from url
        filename = url.split('/')[-1] + '.json'

    try:
        wikidump.dump(url)
        print(wikidump.text)
        #print(wikidump.links)
        #print(wikidump.paragraphs)
    except Exception as e:
        print 'failed to dump data'
        traceback.print_exc()
        sys.exit()
