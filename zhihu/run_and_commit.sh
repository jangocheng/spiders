#!/usr/bin/env bash

python3 zhihu_me.py

git add --all
git commit -m"`date +'%Y-%m-%d'`"
git pull --rebase
git push
