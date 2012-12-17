#!/bin/bash

ln -s ../aflib/article/markup/markdown_exts/*.py `python2 -c 'import markdown; print markdown.__path__[0]'`/extensions
