#!/usr/bin/python
# -*- coding: utf-8 -*-

import requests
from bs4 import BeautifulSoup
from os import linesep


"""Varaiable/statement names conatining the string `soup` are referencing
   html objects that are parsable by BeautifulSoup.
"""

# Minimum length of a sentence
MIN_LEN = 3


class WikiClient(object):

    def __init__(self, wiki_url):
        self._soup = None
        self._links = None
        self._text = None
        self._paragraphs = None
        self._url = wiki_url
        self.dump(wiki_url)

    def dump(self, url):
        page = requests.get(url)
        soup = BeautifulSoup(page.text, 'html.parser')
        self._soup = self._get_cleared_paragraphs_soup(soup)

    @property
    def links(self):
        if not self._links:
            self._links = self._get_links_from_paragraphs_soup()
        return self._links

    @property
    def text(self):
        if not self._text:
            text = ''
            sentences = self._get_sentences_from_paragraphs_soup(
                paragraph_wise=True)
            for sentence in sentences:
                text = text + sentence
            self._text = text
        return self._text

    @property
    def paragraphs(self):
        if not self._paragraphs:
            self._paragraphs = self._text.split(linesep)
        return self._paragraphs

    def _get_sentences_from_paragraphs_soup(self, paragraph_wise=False):
        """Get all sentences from all paragraphs in the given
        paragraph/html object.
        """
        # Result list to store all extrected sentences-
        sentences_in_paragraphs = []

        # Add linebreak if sentences should be ordewred by paragraph.
        seperator = '\n' if paragraph_wise else ''

        # Get all sentences from the given paragraph/html object.
        for paragraph_soup in self._soup:
            sentences_in_paragraph = self._get_sentences_from_paragraph_soup(
                paragraph_soup)

            # Add all sentences to the result list.
            sentences_in_paragraphs = sentences_in_paragraphs + \
                [seperator] + \
                sentences_in_paragraph

        return sentences_in_paragraphs

    def _get_sentences_from_paragraph_soup(self, paragraph_soup):
        """Get all sentences from the given paragraph/html object.
        """
        all_sentences = []

        # Return a list containing all sentences from the paragraph.
        sentences = paragraph_soup.get_text().split('. ')

        for sentence in sentences:
            if not sentence.endswith('.'):
                sentence = sentence + '.'

            # Ensure sentence is an instance of str
            if isinstance(sentence, unicode):
                sentence = sentence.encode('utf-8')
            all_sentences.append(sentence)

        return all_sentences

    def _clear_paragraph_soup(self, paragraph_soup):
        """Remove all tags from the paragraphs except the paragraph <p>
           and link <a> tags.
        """
        for tag in paragraph_soup.findAll():
            if tag.name.lower() not in ["a", "b"]:
                tag.extract()
        return paragraph_soup

    def _get_cleared_paragraphs_soup(self, soup):
        """Extract all paragraphs from the given wiki/html data. Remove
           all other html tags from the paragraphs.
        """
        # Store all paragraphs that contain links in a list.
        cleared_paragraphs_soup = []

        # Find all paragraphs in the data.
        paragraphs_soup = soup.find_all('p')

        # Find the relevant paragraphs.
        for paragraph_soup in paragraphs_soup:
            # Remove html tags from paragraph except for <a> and <p>.
            cleared_paragraph_soup = self._clear_paragraph_soup(paragraph_soup)
            # Add the paragraph to the list if it is not empty.
            if len(cleared_paragraph_soup.get_text()) > MIN_LEN:
                cleared_paragraphs_soup.append(cleared_paragraph_soup)

        return cleared_paragraphs_soup

    def _get_links_from_paragraphs_soup(self):
        """Extract all links from all given paragraphs and return
           a list of the link texts and hrefs.
        """
        # Store link text and href as a dict in a list.
        links = []

        # Find all links in the paragraphs.
        for paragraph_soup in self._soup:
            links_soup = paragraph_soup.find_all('a', href=True)
            for link_soup in links_soup:
                links.append({
                    'text': link_soup.get_text(),
                    'href': link_soup['href']
                    })
        return links
