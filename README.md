<img src="https://upload.wikimedia.org/wikipedia/commons/8/80/Wikipedia-logo-v2.svg"></img>

# WikiDump

Dump Wikipedia articles to file or console. Follow all links in the article recursively.

## Usage

```
-h  --help             show this help message and exit
-u  --url              url of the wiki article
-ul --url-file         path to a file containing all urls
-r  --recursion-depth  depth to follow links recursively
-d  --dump             path to directory for data export
-p  --paragraphs       get the text paaragraph-wise
-t  --text             get the text
-l  --links            get all links from the text
-v  --verbose          print data to stdout
```

**Example**

Dump article *Fashion* and all linked articles to ~/data directory. Extract all links and get the text pragraph-wise.

```python wikidump.py -u https://en.wikipedia.org/wiki/Fashion -r 1 -d ~/data/ -t -p -l```
