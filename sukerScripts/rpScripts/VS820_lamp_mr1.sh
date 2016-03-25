#! /bin/bash

repolr -b repolr -b SAS_msm8916_l_mr1_c50_vzw_ODR_150706 --reference=/home001/mirror/lr
repo sync -cq -d -j4 --no-tags
repo start SAS_msm8916_l_mr1_c50_vzw_ODR_150706 --all
repo forall -c 'git remote set-url --push lr ssh://lr.lge.com:029475/${REPO_PROJECT}'

