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
    partname=("$@")
   
    for i in "${partname[@]}"
    do
	echo "1"
	echo "$i "
    done
}

a=()
a+=("boot_a:emmc")
a+=("boot_b:emmc")
a+=("boot_c:emmc")

aaa "${a[@]}"

function copyFiles() {
    arr=("$@")
    for i in "${arr[@]}";
    do
        echo "$i"
    done
}

array=("one" "two" "three")

copyFiles "${array[@]}"
