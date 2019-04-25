#!/bin/bash

# PARSE target_product files
LGE_BUILD_PATH=android/vendor/lge/build
source ${LGE_BUILD_PATH}/release_common.sh

#_CUPSS_____________________________________________________S
if [ ! -z "$CUPSS_BUILD" ]; then
    echo "------------------------------------"
    echo "[${TARGET_NAME}] is CUPSS_MODEL !"
    echo "------------------------------------"
    export USE_CUPSS=true
    export TARGET_CUPSS_CARRIER=`echo ${CUPSS_BUILD} | awk -F_ '{print $1}'`
    export TARGET_CUPSS_COUNTRY=`echo ${CUPSS_BUILD} | awk -F_ '{print $2}'`
else
    export USE_CUPSS=false
    unset TARGET_CUPSS_CARRIER
    unset TARGET_CUPSS_COUNTRY
fi
#_CUPSS_____________________________________________________E



#_RELEASE_IMAGE_____________________________________________S
if test -z "$2"
then
    if [ "$CHIPSET_VENDOR" != "qcom" ]; then
        ${RELEASE_SCRIPT_PATH}/${CHIPSET_VENDOR}/${CHIPSET_VENDOR}_image.sh
    else
        ${RELEASE_SCRIPT_PATH}/${CHIPSET_VENDOR}/${CHIPSET_NAME}_image.sh
    fi
else
    PARAM=$@;
    CUST_STR=" ";
    for P in $PARAM;
    do
        if [ $1 != $P ]; then
            export CUST_STR=$CUST_STR" "$P;
    fi
    done

    if [ "$CHIPSET_VENDOR" != "qcom" ]; then
        ${RELEASE_SCRIPT_PATH}/${CHIPSET_VENDOR}/${CHIPSET_VENDOR}_image.sh ${CUST_STR}
    else
        ${RELEASE_SCRIPT_PATH}/${CHIPSET_VENDOR}/${CHIPSET_NAME}_image.sh ${CUST_STR}
    fi
fi
#_RELEASE_IMAGE_____________________________________________E



#_SEND_MODEL_INFO___________________________________________S
# make dp_preload & send model information(aqc.lge.com)
# Should be executed in Last build Process ( After LGE Singing, make TOT, Etc )
APPS_SCRIPTS_PATH="android/vendor/lge/apps/Scripts"
if [ -f "${APPS_SCRIPTS_PATH}/send_model_info.sh" ]
then
   ${APPS_SCRIPTS_PATH}/send_model_info.sh ${TARGET_PRODUCT}
fi
#_SEND_MODEL_INFO___________________________________________E
