#! /bin/bash

echo Input tagName:
read tagName
echo good!
echo ''

repolr -b lamp_l_mr1_release -m $tagName.xml --reference=/home001/mirror/lr/
repo sync -cq -d -j4 --no-tags
repo start lamp_l_mr1_release --all
