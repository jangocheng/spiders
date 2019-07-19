#!/usr/bin/env bash

git add --all
git commit -m"`date +'%Y-%m-%d'`"
git pull --rebase
git push