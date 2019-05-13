#!/bin/sh

val1=50
val2=22

test_plus=$((${val1}+${val2}))
test_minus=$((${val1}-${val2}))

echo ${test_plus}
echo ${test_minus}
