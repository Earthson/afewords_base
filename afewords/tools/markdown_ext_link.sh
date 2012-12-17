#!/bin/bash

MARKDOWNEXTS=`cd .. && pwd`/aflib/article/markup/markdown_exts/*.py
ln -s $MARKDOWNEXTS `python2 -c 'import markdown; print markdown.__path__[0]'`/extensions
