#!/bin/bash

python2 refresh_article.py
python2 convert_article_to_markdown.py
python2 unescape_body.py
python2 refresh_article.py
