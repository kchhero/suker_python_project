#!/bin/bash

#this is cscope/c${TAGS_OUT} index build script
#[jongho3.lee@lge.com] 2010.04.17
#

#############variables###########################
REF_DIR=~/workspace/.cscopefiles/
CUR_DIR=`pwd`
BASE_DIR=`basename $CUR_DIR`
PROJECT_NAME=$BASE_DIR

CSCOPE_FILES=cscope.files
CSCOPE_FILES2=cscope.out.in
CSCOPE_FILES3=cscope.out.po
CSCOPE_OUT=cscope.out
TAGS_OUT=tags

############functions#############################
echo $CUR_DIR
############ code ###############################
echo " "
echo "################################### "
if [ $# -gt 1 ] && [ "$2" == "reuse" ]
then
echo "reused cscope files..."
else
echo "building cscope.files ...."

find $CUR_DIR -type f \(  -iname '*.dtb' -o -iname '*.dtsi' -o -iname '*.dts' -o -iname '*.c' -o -iname '*.cpp' -o -iname '*.cc' -o -iname '*.h' -o -iname '*.java' -o -iname '*.jni' -o -iname '*.mk' -o -iname '*.xml' -o -iname '*.aidl' -o -iname '*.s' -o -iname '*.S' -o -iname '*.rc' -o -iname '*_defconfig' -o -iname '*.config' -o -iname 'Makefile' -o -iname 'Kconfig' -o -iname '*.sh' -o -iname '*.min' -o -iname '*.cfg' -o -iname '*.mak' -o -iname 'sconscript' -o -iname '*.cmd' -o -iname '*.cmm' -o -iname '*.txt' \) -print > ${CSCOPE_FILES}
fi

echo " "
echo "################################### "
echo "building cscope.out ...."
cscope -b -q -k -i ${CSCOPE_FILES} -f ${CSCOPE_OUT}

echo " "
echo "################################### "
echo "building ctags ...."
#ctags -R -f ${TAGS_OUT}
ctags -R --sort=1 --c++-kinds=+p --fields=+iaS --extra=+q --language-force=C++ -f ${TAGS_OUT}
#ctags -R --sort=1 --c++-kinds=+p --fields=+iaS --extra=+q --language-force=C++ -f cpp cpp_src

set tags+=${CUR_DIR}

