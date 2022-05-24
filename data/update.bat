@echo off
title "ACT Senate count update"

@echo Gathering data ...
@echo.

git fetch --all
git reset --hard origin/gh-pages

py update_results.py

@echo.
git add .
git commit -m "update"
git push
