#!/bin/bash

# PARSE target_product files
LGE_BUILD_PATH=android/vendor/lge/build
source ${LGE_BUILD_PATH}/release_common.sh

if [ "$CHIPSET_VENDOR" != "qcom" ]; then
    ${RELEASE_SCRIPT_PATH}/${CHIPSET_VENDOR}/${CHIPSET_VENDOR}_elf.sh
else
    ${RELEASE_SCRIPT_PATH}/${CHIPSET_VENDOR}/${CHIPSET_NAME}_elf.sh
fi
#echo ===============================================================
#echo ========== ./release_app_jar.sh ${TARGET_NAME} ================
#echo ===============================================================
#./release_app_jar.sh
