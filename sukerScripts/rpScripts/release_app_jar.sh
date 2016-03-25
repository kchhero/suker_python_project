#!/bin/bash

#App Debugging .jar files
##########################################################################################
# Version        : 1.0
# Make date      : 2013.07.08
# Last Modified  : 2013.11.27
# Make script    : hwanseok.kim@lge.com
###########################################################################################

# pre check if parsed TARGET_PRODUCT
if [ "${PARSED}" != "true" ]
then
    RELEASE_SCRIPT_PATH=android/vendor/lge/build
    source ${RELEASE_SCRIPT_PATH}/release_common.sh
fi

# Local Variable Define
ROOT_DIR=$(echo `pwd`)
echo $ROOT_DIR

cd android
source ./build/envsetup.sh
choosecombo 1 $TARGET_PRODUCT 2
TEMP=`(get_abs_build_var PRODUCT_OUT)`
cd ..

TARGET_OUT=android/${TEMP#*\/android\/}
ANDROID_OUT=${TARGET_OUT%\/target*}
TAG_NAME=$(echo $(grep -w ro.lge.swversion ${TARGET_OUT}/system/build.prop) | sed -e 's/ro.lge.swversion=//;s/^[\t]*//;s/[ \t].*//')
DL_SW_VER=$(echo $(grep -w ro.lge.swversion ${TARGET_OUT}/system/build.prop) | sed -e 's/ro.lge.swversion=//;s/^[ \t]*//;s/[ \t].*//')
DL_SW_REV=$(echo $(grep -w ro.lge.swversion_rev ${TARGET_OUT}/system/build.prop) | sed -e 's/ro.lge.swversion_rev=//;s/^[ \t]*//;s/[ \t].*//')
DL_CARRIER=$(echo $(grep -w ro.build.target_operator ${TARGET_OUT}/system/build.prop) | sed -e 's/ro.build.target_operator=//;s/^[ \t]*//;s/[ \t].*//')

DELIM=_LAMP
IS_INTEGVER=$(echo "${DL_SW_VER}" | grep -e "${DELIM}")
if [ -z "${IS_INTEGVER}" ] ; then
    if [ "$DL_CARRIER" == "USC" ] || [ "$DL_CARRIER" == "LRA" ] || [ "$DL_CARRIER" == "ACG" ] || [ "$DL_CARRIER" == "TRF" ] || [ "$DL_CARRIER" == "SPR" ] ; then
        TAG_NAME=${TAG_NAME}_${DL_SW_REV}
    else
        TAG_NAME=$(echo $(grep -w ro.lge.factoryversion  ${TARGET_OUT}/system/build.prop) | sed -e 's/ro.lge.factoryversion=//;s/^[ \t]*//;s/[ \t].*//')
    fi
fi

# replace TAG_NAME for USC using LA40(Dime4.0)
if [ "$DL_CARRIER" == "USC" ] || [ "$DL_CARRIER" == "ACG" ] ; then
    TAG_NAME=$(echo $TAG_NAME | sed 's/LA20/LA40/g')
fi

#replace TAG name for LA30 model
if [ "$DL_CARRIER" == "CMCC" -o "$DL_CARRIER" == "CTC" -o  "$DL_CARRIER" == "CUCC" -o "$DL_CARRIER" == "CMHK" -o "$DL_CARRIER" == "OPEN" ] ; then
    TAG_NAME=$(echo $TAG_NAME | sed 's/LA20/LA30/g')
fi

RELEASE_APP_JARS_ROOT=RELEASE/${TAG_NAME}/DEBUG
RELEASE_APP_JARS_OUT=${RELEASE_APP_JARS_ROOT}/${TARGET_PRODUCT}/App_Jars

#JAVA_LIBRARIES ROOT
JAVA_LIBRARIES_COMMON_ROOT=$ANDROID_OUT/target/common/obj/JAVA_LIBRARIES/

searchfileName=attach_jar_list.txt
defaultjarName=classes-full-debug.jar
classjarName=classes.jar

#echo "Debbuing Code ----------------------------------------------------"
#echo "TEMP = $TEMP"
#echo "TARGET_PRODUCT = $TARGET_PRODUCT"
#echo "TARGET_DEVICE = $TARGET_DEVICE"
#echo "Android_out = $ANDROID_OUT"
#echo "Taget_Out = $TARGET_OUT"
#echo "Tag_Name = $TAG_NAME"
#echo "RELEASE_APP_JARS_ROOT = $RELEASE_APP_JARS_ROOT"
#echo "RELEASE_APP_JARS_OUT = $RELEASE_APP_JARS_OUT"
#echo "JAVA_LIBRARIES_COMMON_ROOT = $JAVA_LIBRARIES_COMMON_ROOT"
#echo "Debbuing Code ----------------------------------------------------"


#Debug Folder Check
if [ ! -d $RELEASE_APP_JARS_OUT ]
then
    mkdir -p $RELEASE_APP_JARS_OUT
    sleep 3 #Make Folder Delay Time
fi

cd $JAVA_LIBRARIES_COMMON_ROOT
$(echo "ls -A") > $searchfileName
sleep 5 #delay time

duplicateCN="0"
for item in $(cat $searchfileName)
do
#    #Directory Check
    if [ -d $item ]
    then
        cd $item
    item_low=`echo $item | tr A-Z a-z`
    if [ -f $ROOT_DIR/$RELEASE_APP_JARS_OUT/$item_low.jar ]
    then
            duplicateCN=$(($duplicateCN+1))
            item_low=$item_low$duplicateCN
    else
        duplicateCN="0"
        fi

        if [ -e $defaultjarName ]
        then
            cp $defaultjarName $ROOT_DIR/$RELEASE_APP_JARS_OUT/$item_low.jar
        elif [ -e $classjarName ]
        then
            cp $classjarName $ROOT_DIR/$RELEASE_APP_JARS_OUT/$item_low.jar
        else
            echo "Fail : Root Directory or Don't *.jar"
        fi
        cd -
    else
        echo "Fail : Non-Directory"
    fi #if [ $DirChk = "1" ]
done
rm -rf $searchfileName
cd -
