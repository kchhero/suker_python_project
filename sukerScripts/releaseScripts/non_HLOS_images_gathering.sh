#!/bin/sh

mkdir __non_HLOS_images__
cp ./common/build/gpt_both0.bin ./non_HLOS_images
cp ./boot_images/build/ms/bin/8916/sbl1.mbn ./non_HLOS_images
cp ./rpm_proc/build/ms/bin/8916/rpm.mbn ./non_HLOS_images
cp ./trustzone_images/build/ms/bin/MAVAANAA/tz.mbn ./non_HLOS_images
cp ./trustzone_images/build/ms/bin/MAVAANAA/hyp.mbn ./non_HLOS_images
cp ./common/build/bin/asic_8916/NON-HLOS.bin ./non_HLOS_images

mkdir __restore_images__
cp ./boot_images/core/storage/tools/ptool/flash.xml ./__restore_images__
cp ./boot_images/build/ms/bin/EMMCBLD/8916_msimage.mbn ./__restore_images__
cp ./boot_images/build/ms/bin/8916/MPRG8916.mbn ./__restore_images__
