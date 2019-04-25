#!/bin/bash

#sed '/bootargs=/a hello' test.txt

#sed -ne 's/bootargs=/ :SUFFIX &/p' test.txt

#sed -i '/bootargs=/a Hello World' test.txt

#sed  -e '/tc_/s/$/ status=D/'

#sed -i 's/bootargss=/abc/g' test.txt

#sed -i "/bootargs=/aBabo" ./test.txt

#awk '/bootargs=/babo' test.txt

sed -i -e '/^bootargs=/ s/$/ anotherthing/' test.txt
