#!/usr/bin/env bash

msg=`python3 zhihu_me.py`

git add --all .
git commit -m "${msg}"
git pull --rebase
git push
