#!/bin/bash

function bbb()
{
    local n=()
    n="$@"

    for j in ${n[@]}
    do
	echo $j
    done
}

function aaa()
{
    local partname=()
    partname="$@"
   
    local ccc=()

    for i in ${partname[@]}
    do
	echo "1"
	echo "$i "
	ccc+=$i
    done

    echo "ccc1 = ${@:1:1}"
    echo "ccc1 = ${@:2:1}"
    echo "ccc1 = ${@:3:1}"
}

a1="boot_a:emmc"
b2="boot_b:emmc"
c3="boot_c:emmc"

aaa $a1 $b2 $c3

