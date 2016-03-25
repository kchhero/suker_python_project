#!/bin/bash

# PARSE target_product files
LGE_BUILD_PATH=android/vendor/lge/build
source ${LGE_BUILD_PATH}/release_common.sh

if test -z "$2"
then
    if [ "$CHIPSET_VENDOR" != "qcom" ]; then
        ${RELEASE_SCRIPT_PATH}/${CHIPSET_VENDOR}/${CHIPSET_VENDOR}_image_factory.sh
    else
        ${RELEASE_SCRIPT_PATH}/${CHIPSET_VENDOR}/${CHIPSET_NAME}_image_factory.sh
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
        ${RELEASE_SCRIPT_PATH}/${CHIPSET_VENDOR}/${CHIPSET_VENDOR}_image_factory.sh $2
    else
        ${RELEASE_SCRIPT_PATH}/${CHIPSET_VENDOR}/${CHIPSET_NAME}_image_factory.sh ${CUST_STR}
    fi
fi
