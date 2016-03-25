#!/bin/sh

mkdir non_HLOS_images
cp ./common/build/gpt_both0.bin ./non_HLOS_images
cp ./boot_images/build/ms/bin/8x26/sbl1.mbn ./non_HLOS_images
cp ./rpm_proc/build/ms/bin/AAAAANAAR/rpm.mbn ./non_HLOS_images
cp ./trustzone_images/build/ms/bin/FARAANBA/tz.mbn ./non_HLOS_images
cp ./debug_image/build/ms/bin/AAAAANAZ/sdi.mbn ./non_HLOS_images
cp ./common/build/bin/asic/NON-HLOS.bin ./non_HLOS_images
