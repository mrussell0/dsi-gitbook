#!/bin/bash

# script to pull in recent changes from hq

git remote add upstream https://github.com/generalassembly-studio/dsi-course-materials
git fetch upstream
git checkout master
git rebase upstream/master
