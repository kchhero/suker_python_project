#! /bin/bash

echo Input tagName:
read tagName
echo good!
echo ''

repolr -b msm8916_l_cy_trf_us_mp_141230 -m $tagName.xml --reference=/home001/mirror/lr/
repo sync -cq -d -j4 --no-tags
repo start msm8916_l_cy_trf_us_mp_141230 --all
