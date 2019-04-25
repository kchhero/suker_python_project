#!/bin/bash

function abc()
{
    arg1=$1; shift
    array=( "$@" )
    last_idx=$(( ${#array[@]} - 1 ))
    
    arg2=${array[$last_idx]}
    unset array[$last_idx]

    echo "arg1=$arg1"
    echo "arg2=$arg2"
    echo "array contains:"
    printf "%s\n" "${array[@]}"
}

ttt=("two" "three")
abc "one" "${ttt[@]}" "four"



function def()
{
    arg1="$1"
    arg2=("${!2}")
    arg3="$3"
    arg4=("${!4}")

    echo "arg1=$arg1"
    echo "arg2 array=${arg2[@]}"
    echo "arg2 #elem=${#arg2[@]}"
    echo "arg3=$arg3"
    echo "arg4 array=${arg4[@]}"
    echo "arg4 #elem=${#arg4[@]}"
}

arr=(ab 'x y' 123)
arr2=(a1 'a a' bb cc 'it is one')

def "foo" "arr[@]" "bar" "arr2[@]"
