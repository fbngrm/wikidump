#!/usr/bin/python
import argparse


def parse():
        """parse arguments supplied by cmd-line
        """
        parser = argparse.ArgumentParser(
            description='WikiDump - dump wikipedia articles to a file.',
            formatter_class=argparse.RawTextHelpFormatter
            )
        group = parser.add_mutually_exclusive_group()
        group.add_argument(
            '-u',
            '--url',
            help='url of the wiki article',
            required=False,
            metavar='',
            )
        group.add_argument(
            '-ul',
            '--url-file',
            help='path to a file containing all urls',
            required=False,
            metavar='',
            )

        parser.add_argument(
            '-r',
            '--recursion-depth',
            metavar='',
            help='depth to follow links recursively',
            required=False,
            )
        parser.add_argument(
            '-d',
            '--dump',
            metavar='',
            help='path to directory for data export',
            required=False,
            )
        parser.add_argument(
            '-p',
            '--paragraphs',
            help='get the text paaragraph-wise',
            required=False,
            action='store_true',
            )
        parser.add_argument(
            '-t',
            '--text',
            help='get the text',
            required=False,
            action='store_true',
            )
        parser.add_argument(
            '-l',
            '--links',
            help='get all links from the text',
            required=False,
            action='store_true',
            )
        parser.add_argument(
            '-v',
            '--verbose',
            help='print data to stdout',
            required=False,
            action='store_true',
            )

        return vars(parser.parse_args())
