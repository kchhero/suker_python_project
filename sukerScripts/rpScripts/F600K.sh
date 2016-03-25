#! /bin/bash

echo Input tagName:
read tagName
echo good!
echo ''

repolr -b msm8992_l_mr1_pplus_mp_150825 -m $tagName.xml --reference=/home001/mirror/lr/
repo sync -cq -d -j4 --no-tags
repo start msm8992_l_mr1_pplus_mp_150825 --all
