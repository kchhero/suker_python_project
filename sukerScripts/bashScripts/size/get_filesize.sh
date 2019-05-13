#!/bin/sh

filename=get_filesize.sh

file_size_b=`du -b "$filename" | cut -f1`
file_size_kb=`du -k "$filename" | cut -f1`

echo "${file_size_b} byte"
echo "${file_size_kb} Kbyte"
