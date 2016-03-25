#! /bin/bash

repolr -b lamp_l_mr1_release -m msm8916/msm8916-recent.xml
repo sync -cq -d -j4 --no-tags
repo start lamp_l_mr1_release --all
repo forall -c 'git remote set-url --push lr ssh://lr.lge.com:029475/${REPO_PROJECT}'

