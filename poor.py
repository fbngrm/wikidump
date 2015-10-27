#!/usr/bin/python
# -*- coding: utf-8 -*-

import requests
import re
from bs4 import BeautifulSoup

def get_sentences_with_links(paragraph_soup):
    """Get all sentences that contain links from the given 
       paragraph/html object.
    """

    # Store all sentences containing links in a list.
    sentences_with_links = []

    # Strip the <p> tag from the paragraph.
    without_p_tag = str(paragraph)[3:-4]

    # Create a list containing all sentences from the paragraph.
    sentences = without_p_tag.split('. ')

    # Filter the sentences containing no links.
    for sentence in sentences:

        # Skip the sentences that do not contain links.
        if '</a>' not in sentence:
            continue

        # Add to the restult list.
        sentences_with_links.append(BeautifulSoup(sentence, 'html.parser'))

    return sentences_with_links


def get_paragraphs(soup):
    """Extract all paragraphs from the given wiki/html data that 
       contain links. Remove all other html tags from the paragraphs.
    """

    # Store all paragraphs that contain links in a list.
    paragraphs = []

    # Find all paragraphs in the data.
    paragraph_soup = soup.find_all('p')

    # Find the relevant paragraphs.
    for paragraph in paragraph_soup:
        # Skip paragraphs when they do not contain any link/entity.
        if not paragraph.a:
            continue

        # Remove all tags from the paragraphs except the paragraph <p> and link <a> tags.
        for tag in paragraph.findAll():
            if tag.name.lower() not in "a":
                tag.extract()

        # Add the paragraph to the list.
        paragraphs.append(paragraph)

    return paragraphs

if __name__ == '__main__':
    wiki_url = 'https://en.wikipedia.org/wiki/Fashion'
    page = requests.get(wiki_url)
    soup = BeautifulSoup(page.text, 'html.parser')

    paragraphs = get_paragraphs(soup)

    for paragraph in paragraphs:
        sentences_in_paragraph = get_sentences_with_links(paragraph)

    for sentence in sentences_in_paragraph:
        links = sentence.find_all('a')
        print(sentence.get_text().split(links[0].get_text(), 1))
        print(links)

        #pieces = re.compile(r'<a(.*?)a>').split(sentence)
