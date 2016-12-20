#!/bin/bash

# Copyright (c) 2016 Nexell Co., Ltd.
# Author: Sungwoo, Park <swpark@nexell.co.kr>
# 
# Permission is hereby granted, free of charge, to any person obtaining a copy of
# this software and associated documentation files (the "Software"), to deal in
# the Software without restriction, including without limitation the rights to
# use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of
# the Software, and to permit persons to whom the Software is furnished to do so,
# subject to the following conditions:
# 
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
# 
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS
# FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR
# COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER
# IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN
# CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.

set -e

TOP=`pwd`
export TOP

SCRIPT_DIR=`dirname "$(readlink -f "$0")"`
CONFIG_DIR=$SCRIPT_DIR/../configs

BUILD_ALL=true
BUILD_BL1=false
BUILD_UBOOT=false
BUILD_OPTEE=false
BUILD_KERNEL=false
BUILD_MODULE=false
BUILD_USER=false
BUILD_BUILDROOT=false
BUILD_HWTEST=false
VERBOSE=false
CHECK_BRANCH=true
MEM_SIZE=1024

RELEASE_VERSION=
RELEASE_DATE=
UBOOT_VERSION=
KERNEL_VERSION=

BOARD_NAME=

BOARD_PREFIX=
BOARD_PURENAME=

RESULT_DIR=

ARM_ARCH=arm64
CHIP_NAME=s5p6818

# 32MiB
BOOT_PARTITION_SIZE=33554432
# 32MiB
MODULES_PATITION_SIZE=33554432
# 3800MiB
ROOT_PARTITION_SIZE=3984588800

function usage()
{
	echo "Usage: $0 -b <board-name> [-m memsize -t bl1 -t u-boot -t optee -t kernel -t module -t user -n -v]"
	echo -e '\n -b <board-name> : target board name'
	echo " -m memsize : 512, 1024, 2048 board memory size, unit size MB, default 1024"
	echo " -d <result-directory] : specify result directory instead of default result dir"
	echo " -t bl1    : if you want to build only u-boot, specify this, default no"
	echo " -t u-boot : if you want to build only u-boot, specify this, default no"
	echo " -t optee  : if you want to build only optee, specify this, default no"
	echo " -t kernel : if you want to build only kernel, specify this, default no"
	echo " -t optee-module : if you want to build only optee module, specify this, default no"
	echo " -t user   : if you want to build only user app, specify this, default no"
	echo " -t buildroot   : if you want to build buildroot, specify this, default no"
	echo " -t hwtest : if you want to build hwtest, specify this, default no"
	echo " -n : if you want to disable check branch, specify this, default no"
	echo " -v : if you want to view verboase build log message, specify this, default no"
	echo " -V Version: Release version"
	echo " -D Date: Release date"
}

function vmsg()
{
	local verbose=${VERBOSE:-"false"}
	if [ ${verbose} == "true" ]; then
		echo "$@"
	fi  
}

function parse_args()
{
	TEMP=`getopt -o "b:t:m:hnvV:d:D:" -- "$@"`
	eval set -- "$TEMP"

	while true; do
		case "$1" in
			-b ) BOARD_NAME=$2; shift 2 ;;
			-m ) MEM_SIZE=$2; shift 2 ;;
			-d ) RESULT_DIR=`readlink -e $2`; shift 2 ;;
			-t ) case "$2" in
				bl1    ) BUILD_ALL=false; BUILD_BL1=true ;;
				u-boot ) BUILD_ALL=false; BUILD_UBOOT=true ;;
				optee  ) BUILD_ALL=false; BUILD_OPTEE=true ;;
				kernel ) BUILD_ALL=false; BUILD_KERNEL=true ;;
				optee-module ) BUILD_ALL=false; BUILD_MODULE=true ;;
				user   ) BUILD_ALL=false; BUILD_USER=true ;;
				buildroot ) BUILD_BUILDROOT=true ;;
				hwtest ) BUILD_HWTEST=true ;;
				none   ) BUILD_ALL=false ;;
			     esac
			     shift 2 ;;
			-h ) usage; exit 1 ;;
			-v ) VERBOSE=true; shift 1 ;;
			-n ) CHECK_BRANCH=false; shift 1 ;;
			-V ) RELEASE_VERSION=$2; shift 2;;
			-D ) RELEASE_DATE=$2; shift 2;;
			-- ) break ;;
		esac
	done
}

function parse_config()
{
	configfile=$1
	shopt -s extglob
	while IFS='= ' read lhs rhs
	do
		if [[ ! $lhs =~ ^\ *# && -n $lhs ]]; then
			rhs="${rhs%%\#*}"    # Del in line right comments
			rhs="${rhs%%*( )}"   # Del trailing spaces
			rhs="${rhs%\"*}"     # Del opening string quotes
			rhs="${rhs#\"*}"     # Del closing string quotes
			export $lhs=$rhs
		fi
	done < $configfile
}

function print_args()
{
	vmsg "================================================="
	vmsg " print args"
	vmsg "================================================="
	vmsg -e "BOARD_NAME:\t\t${BOARD_NAME}"
	vmsg -e "MEM_SIZE:\t\t${MEM_SIZE}MB"
	if [ ${BUILD_ALL} == "true" ]; then
		vmsg -e "Build:\t\t\tAll"
	else
		if [ ${BUILD_BL1} == "true" ]; then
			vmsg -e "Build:\t\t\tbl1"
		fi
		if [ ${BUILD_UBOOT} == "true" ]; then
			vmsg -e "Build:\t\t\tu-boot"
		fi
		if [ ${BUILD_OPTEE} == "true" ]; then
			vmsg -e "Build:\t\t\toptee"
		fi
		if [ ${BUILD_KERNEL} == "true" ]; then
			vmsg -e "Build:\t\t\tkernel"
		fi
		if [ ${BUILD_MODULE} == "true" ]; then
			vmsg -e "Build:\t\t\toptee-module"
		fi
		if [ ${BUILD_USER} == "true" ]; then
			vmsg -e "Build:\t\t\tuser"
		fi
		if [ ${BUILD_BUILDROOT} == "true" ]; then
			vmsg -e "Build:\t\t\tbuildroot"
		fi
		if [ ${CHECK_BRANCH} == "true" ]; then
			vmsg -e "Check branch all repositories"
		fi
	fi
	vmsg
}

function check_board_name()
{
	local board_name=${1}

	if [ -z ${board_name} ]; then
		echo "You must specify board name!!!"
		exit 1
	fi
}

function get_board_prefix()
{
	BOARD_PURENAME=${BOARD_NAME#*_}
	BOARD_PREFIX=${BOARD_NAME%_*}
	echo "BOARD_PURENAME --> ${BOARD_PURENAME}"
	echo "BOARD_PREFIX --> ${BOARD_PREFIX}"
}

function check_branch()
{
	local branch=$(git branch | awk '{print $2}' | tr -d [[:space:]])
	echo -n "check branch artik: $(pwd) ---> "
	if [ "${branch}" != "artik" ]; then
		echo "source branch must be artik!!!"
		echo "$(pwd) is not branch artik"
		echo "do following and retry =====> "
		echo "# repo forall -c git checkout artik"
		exit -1
	fi
	echo "done"
}

function check_all_branch()
{
	for d in $(ls -l | grep "^d" | awk '{print $9}'); do
		cd ${d}
		if [ -d ".git" ]; then
			check_branch
		fi
		cd ..
	done
}

function setup_toolchain()
{
	if [ ! -f ${TOP}/tools-artik7/toolchain/arm-eabi-4.8/bin/arm-eabi-gcc ]; then
		cd ${TOP}/tools-artik7/toolchain
		tar xJf arm-eabi-4.8.tar.xz
		cd ${TOP}
	fi
	export PATH=${TOP}/tools-artik7/toolchain/arm-eabi-4.8/bin:$PATH

	if [ ! -f ${TOP}/tools-artik7/toolchain/gcc-linaro-aarch64-none-elf-4.8-2014.04_linux/bin/aarch64-none-elf-gcc ]; then
		cd ${TOP}/tools-artik7/toolchain
		tar xJf gcc-linaro-aarch64-none-elf-4.8-2014.04_linux.tar.xz
		cd ${TOP}
	fi
	export PATH=${TOP}/tools-artik7/toolchain/gcc-linaro-aarch64-none-elf-4.8-2014.04_linux/bin:$PATH

	if [ ! -f ${TOP}/tools-artik7/toolchain/gcc-linaro-4.9-2014.11-x86_64_arm-linux-gnueabihf/bin/arm-linux-gnueabihf-gcc ]; then
		cd ${TOP}/tools-artik7/toolchain
		tar xJf gcc-linaro-4.9-2014.11-x86_64_arm-linux-gnueabihf.tar.xz
		cd ${TOP}
	fi
	export PATH=${TOP}/tools-artik7/toolchain/gcc-linaro-4.9-2014.11-x86_64_arm-linux-gnueabihf/bin:$PATH

	if [ ! -f ${TOP}/tools-artik7/toolchain/gcc-linaro-4.9-2015.05-x86_64_aarch64-linux-gnu/bin/aarch64-linux-gnu-gcc ]; then
		cd ${TOP}/tools-artik7/toolchain
		tar xJf gcc-linaro-4.9-2015.05-x86_64_aarch64-linux-gnu.tar.xz
		cd ${TOP}
	fi
	export PATH=${TOP}/tools-artik7/toolchain/gcc-linaro-4.9-2015.05-x86_64_aarch64-linux-gnu/bin:$PATH

	if [ ! -f ${TOP}/tools-artik7/toolchain/gcc-linaro-4.9-2015.05-x86_64_arm-linux-gnueabi/bin/arm-linux-gnueabi-gcc ]; then
		cd ${TOP}/tools-artik7/toolchain
		tar xJf gcc-linaro-4.9-2015.05-x86_64_arm-linux-gnueabi.tar.xz
		cd ${TOP}
	fi
	export PATH=${TOP}/tools-artik7/toolchain/gcc-linaro-4.9-2015.05-x86_64_arm-linux-gnueabi/bin:$PATH
}

function get_cross_compile_prefix()
{
	if [ "${ARM_ARCH}" == "arm64" ]; then
		echo -n "aarch64-linux-gnu"
	else
		echo -n "arm-linux-gnueabi"
	fi
}

function build_bl1()
{
	if [ ${BUILD_ALL} == "true" ] || [ ${BUILD_BL1} == "true" ]; then
		echo ""
		echo "================================================="
		echo "build bl1"
		echo "================================================="

		local bl1_source=
		if [ "${ARM_ARCH}" == "arm64" ]; then
			bl1_source=${TOP}/bl1-artik7
		else
			bl1_source=${TOP}/bl1-artik530
		fi
		local upper_board_name=$(echo "$BOARD_PURENAME" | awk '{print toupper($0)}')
		cd ${bl1_source}
		make clean
		make BOARD=${upper_board_name}
		cd ${TOP}
	fi
}

function build_uboot_env_param()
{
	local compiler_prefix=${1}

	cp `find . -name "env_common.o"` copy_env_common.o
	${compiler_prefix}objcopy -O binary --only-section=.rodata.default_environment `find . -name "copy_env_common.o"`
	tr '\0' '\n' < copy_env_common.o > default_envs.txt
	cp default_envs.txt default_envs.txt.orig
	tools/mkenvimage -s 16384 -o params.bin default_envs.txt

	# Generate recovery param
	sed -i -e 's/rootdev=0/rootdev=1/g' default_envs.txt
	sed -i -e 's/bootcmd=run ramfsboot/bootcmd=run recoveryboot/g' default_envs.txt
	tools/mkenvimage -s 16384 -o params_recovery.bin default_envs.txt

	# Generate mmcboot param
	sed -i -e 's/bootcmd=run ramfsboot/bootcmd=run mmcboot/g' default_envs.txt.orig
	tools/mkenvimage -s 16384 -o params_mmcboot.bin default_envs.txt.orig

	# Generate sd-boot param
	sed -i -e 's/rootdev=0/rootdev=1/g' default_envs.txt.orig
	tools/mkenvimage -s 16384 -o params_sdboot.bin default_envs.txt.orig

	# Generate hwtest sd-boot param
	sed -i -e 's/bootcmd=run mmcboot/bootcmd=run hwtestboot/g' default_envs.txt.orig
	tools/mkenvimage -s 16384 -o params_hwtest.bin default_envs.txt.orig

	rm copy_env_common.o default_envs.txt default_envs.txt.orig
}

function build_uboot()
{
	if [ ${BUILD_ALL} == "true" ] || [ ${BUILD_UBOOT} == "true" ]; then
		echo ""
		echo "================================================="
		echo "build u-boot"
		echo "================================================="

		cd ${TOP}/u-boot-artik7

		local config=
		if [ ${BOARD_NAME} == ${BOARD_PURENAME} ]; then
			config=s5p6818_arm64_${BOARD_NAME}
		else
			config=${BOARD_NAME}
		fi

		make clean
		make ${config}_config

		cross_compile=$(get_cross_compile_prefix)-
		if [ "${RELEASE_VERSION}" != "" ]; then
			make CROSS_COMPILE=${cross_compile} EXTRAVERSION="-$RELEASE_VERSION" -j8
		else
			make CROSS_COMPILE=${cross_compile} -j8
		fi

		build_uboot_env_param ${cross_compile}

		PLAIN_VERSION=`cat include/generated/version_autogenerated.h | grep "define PLAIN_VERSION" | awk -F \" '{print $2}'`
		UBOOT_VERSION="U-Boot $PLAIN_VERSION"
		cd ${TOP}

		if [ "${ARM_ARCH}" == "arm64" ]; then
			local uart_base=
			if [ ${BOARD_NAME} == ${BOARD_PURENAME} ]; then
				# ex> drone : use uart0
				uart_base=0xc00a1000
			else
				# ex> artik710_raptor : use uart3
				uart_base=0xc00a3000
			fi

			if [ ${BUILD_UBOOT} == "true" ]; then
				make -f optee_build/Makefile PLAT_DRAM_SIZE=${MEM_SIZE} PLAT_UART_BASE=${uart_base} build-fip -j8
				make -f optee_build/Makefile PLAT_DRAM_SIZE=${MEM_SIZE} PLAT_UART_BASE=${uart_base} build-singleimage -j8
			fi
		fi
	fi
}

function build_optee()
{
	if [ ${BUILD_ALL} == "true" ] || [ ${BUILD_OPTEE} == "true" ]; then
		echo ""
		echo "================================================="
		echo "build optee"
		echo "================================================="

		local uart_base=
		if [ ${BOARD_NAME} == ${BOARD_PURENAME} ]; then
			# ex> drone : use uart0
			uart_base=0xc00a1000
		else
			# ex> artik710_raptor : use uart3
			uart_base=0xc00a3000
		fi

		make -f optee_build/Makefile clean
		make -f optee_build/Makefile PLAT_DRAM_SIZE=${MEM_SIZE} PLAT_UART_BASE=${uart_base} build-bl1 -j8
		make -f optee_build/Makefile PLAT_DRAM_SIZE=${MEM_SIZE} PLAT_UART_BASE=${uart_base} build-lloader -j8
		make -f optee_build/Makefile PLAT_DRAM_SIZE=${MEM_SIZE} PLAT_UART_BASE=${uart_base} build-bl32 -j8
		make -f optee_build/Makefile PLAT_DRAM_SIZE=${MEM_SIZE} PLAT_UART_BASE=${uart_base} build-fip -j8
		make -f optee_build/Makefile PLAT_DRAM_SIZE=${MEM_SIZE} PLAT_UART_BASE=${uart_base} build-singleimage -j8
	fi
}

function build_kernel()
{
	if [ ${BUILD_ALL} == "true" ] || [ ${BUILD_KERNEL} == "true" ]; then
		echo ""
		echo "================================================="
		echo "build kernel"
		echo "================================================="

		cd ${TOP}/linux-artik7
		make ARCH=${ARM_ARCH} distclean
		local dts_file=
		if [ ${BOARD_NAME} == ${BOARD_PURENAME} ]; then
			make ARCH=${ARM_ARCH} s5p6818_${BOARD_NAME}_defconfig
			if [ "${CHIP_NAME}" == "s5p6818" ]; then
				dts_file=arch/${ARM_ARCH}/boot/dts/nexell/${CHIP_NAME}-${BOARD_NAME}.dts
			else
				dts_file=arch/${ARM_ARCH}/boot/dts/${CHIP_NAME}-${BOARD_NAME}.dts
			fi
		else
			make ARCH=${ARM_ARCH} ${BOARD_NAME}_defconfig
			if [ "${CHIP_NAME}" == "s5p6818" ]; then
				dts_file=arch/${ARM_ARCH}/boot/dts/nexell/${CHIP_NAME}-${BOARD_PREFIX}.dtsi
			else
				dts_file=arch/${ARM_ARCH}/boot/dts/${CHIP_NAME}-${BOARD_PREFIX}.dtsi
			fi
		fi

		local cross_compile=$(get_cross_compile_prefix)-
		if [ "${RELEASE_VERSION}" != "" ]; then
			make ARCH=${ARM_ARCH} CROSS_COMPILE=${cross_compile} Image EXTRAVERSION="-$RELEASE_VERSION" -j8
			make ARCH=${ARM_ARCH} CROSS_COMPILE=${cross_compile} EXTRAVERSION="-$RELEASE_VERSION" dtbs
			make ARCH=${ARM_ARCH} CROSS_COMPILE=${cross_compile} EXTRAVERSION="-$RELEASE_VERSION" modules -j8
			KERNEL_VERSION="4.1.15-$RELEASE_VERSION"
		else
			make ARCH=${ARM_ARCH} CROSS_COMPILE=${cross_compile} Image -j8
			make ARCH=${ARM_ARCH} CROSS_COMPILE=${cross_compile} dtbs
			make ARCH=${ARM_ARCH} CROSS_COMPILE=${cross_compile} modules -j8
			KERNEL_VERSION="4.1.15"
		fi

		cd ${TOP}
	fi
}

function build_optee_module()
{
	if [ ${BUILD_ALL} == "true" ] || [ ${BUILD_OPTEE_MODULE} == "true" ]; then
		echo ""
		echo "================================================="
		echo "build optee module"
		echo "================================================="

		if [ "${RELEASE_VERSION}" != "" ]; then
			make -C linux-artik7 ARCH=arm64 CROSS_COMPILE=aarch64-linux-gnu- \
				EXTRAVERSION="-$RELEASE_VERSION" M=${TOP}/optee_linuxdriver clean
			make -C linux-artik7 ARCH=arm64 CROSS_COMPILE=aarch64-linux-gnu- \
				EXTRAVERSION="-$RELEASE_VERSION" M=${TOP}/optee_linuxdriver modules -j8
		else
			make -C linux-artik7 ARCH=arm64 CROSS_COMPILE=aarch64-linux-gnu- LOCALVERSION= M=${TOP}/optee_linuxdriver clean
			make -C linux-artik7 ARCH=arm64 CROSS_COMPILE=aarch64-linux-gnu- LOCALVERSION= M=${TOP}/optee_linuxdriver modules -j8
		fi
	fi
}

function print_autogen_fail_msg()
{
	echo -e "\033[1;4;31m[Error in autogen.sh for ${1}]"
	echo "do this command"
	echo "# sudo apt-get install libpciaccess-dev autoconf autogen xutils-dev libtool libpthread-stubs0-dev"
	echo -e "\033[0m"
}

function print_error_msg()
{
	echo -e "\033[1;4;31m[Error in ${1}]\033[0m"
}

function build_user()
{
	if [ ${BUILD_ALL} == "true" ] || [ ${BUILD_USER} == "true" ]; then
		echo ""
		echo "================================================="
		echo "build user"
		echo "================================================="

		mkdir -p sysroot/include
		mkdir -p sysroot/lib
		mkdir -p sysroot/bin
		mkdir -p sysroot/etc

		local cross_compile=$(get_cross_compile_prefix)

		cd ${TOP}/nx-v4l2
		# test -f Makefile && make install || make -f Makefile.cross install
		./autogen.sh || print_autogen_fail_msg nx-v4l2
		./configure --target=${cross_compile} --host=${cross_compile} --build=x86_64-unknown-linux-gnu --prefix=${TOP}/sysroot || print_error_msg "configure nx-v4l2"
		make clean
		make -j8 && make install || print_error_msg "make nx-v4l2"
		cd ${TOP}

		cd ${TOP}/nx-drm-allocator
		# test -f Makefile && make install || make -f Makefile.cross install
		./autogen.sh || print_autogen_fail_msg nx-drm-allocator
		./configure --target=${cross_compile} --host=${cross_compile} --build=x86_64-unknown-linux-gnu --prefix=${TOP}/sysroot || print_error_msg "configure nx-drm-allocator"
		make clean
		make -j8 && make install || print_error_msg "make nx-drm-allocator"
		cd ${TOP}

		# If failed to build libdrm, do below command
		# sudo apt-get install libpciaccess-dev autoconf autogen xutils-dev libtool libpthread-stubs0-dev
		cd ${TOP}/libdrm
		./autogen.sh || print_autogen_fail_msg libdrm
		./configure  --target=${cross_compile} --host=${cross_compile} --build=x86_64-unknown-linux-gnu --prefix=${TOP}/sysroot --disable-dependency-tracking --enable-static --enable-shared --disable-cairo-tests --disable-manpages --disable-intel --disable-radeon --disable-amdgpu --disable-nouveau --disable-vmwgfx --disable-omap-experimental-api --disable-exynos-experimental-api --disable-freedreno --enable-nexell --disable-tegra-experimental-api --disable-udev --disable-valgrind --enable-install-test-programs || print_error_msg "configure libdrm"
		make clean
		make -j8 && make install || print_error_msg "make libdrm"
		cd ${TOP}

		cd ${TOP}/nx-renderer
		# test -f Makefile && make install || make -f Makefile.cross install || echo "failed to build nx-renderer"
		./autogen.sh || print_autogen_fail_msg nx-renderer
		./configure --target=${cross_compile} --host=${cross_compile} --build=x86_64-unknown-linux-gnu --prefix=${TOP}/sysroot --with-extrapath=${TOP}/buildroot/output/staging/usr --with-extrapath_lib=${TOP}/buildroot/output/target/usr/lib --with-extrapath_include=${TOP}/buildroot/output/staging/usr/include || print_error_msg "configure nx-renderer"
		make clean
		make -j8 && make install || print_error_msg "make nx-renderer"
		cd ${TOP}

		cd ${TOP}/nx-scaler
		./autogen.sh || print_autogen_fail_msg nx-scaler
		./configure --target=${cross_compile} --host=${cross_compile} --build=x86_64-unknown-linux-gnu --prefix=${TOP}/sysroot --with-extrapath=${TOP}/buildroot/output/staging/usr --with-extrapath_lib=${TOP}/buildroot/output/target/usr/lib --with-extrapath_include=${TOP}/buildroot/output/staging/usr/include || print_error_msg "configure nx-scaler"
		make clean
		make -j8 && make install || print_error_msg "make nx-scaler"
		cd ${TOP}

		cd ${TOP}/nx-video-api
		./autogen.sh || print_autogen_fail_msg nx-video-api
		./configure --target=${cross_compile} --host=${cross_compile} --build=x86_64-unknown-linux-gnu --prefix=${TOP}/sysroot || print_error_msg "configure nx-video-api"
		make clean
		make -j8 && make install || print_error_msg "make nx-video-api"
		cd ${TOP}

		cd ${TOP}/testsuite
		make clean
		make CROSS_COMPILE=${cross_compile}- || print_error_msg "make testsuite"
		cd ${TOP}

		# OMX-IL
		#cd ${TOP}/libomxil-nx
		#make && make copy INSTALL_DIR="../sysroot/lib/" && make config_file || echo "failed to build libonxil-nx!!"
		#cd ${TOP}

		if [ "${ARM_ARCH}" == "arm64" ]; then
			make -f optee_build/Makefile build-optee-client
			make -f optee_build/Makefile build-optee-test
		fi

		# below commands will fail if buildroot build result is not exist.
		cd ${TOP}/gst-plugins-renderer
		# test -f Makefile && make install || make -f Makefile.cross install || echo "You must build buildroot before build gst-plugins-renderer"
		./autogen.sh || print_autogen_fail_msg gst-plugins-renderer
		./configure --target=${cross_compile} --host=${cross_compile} --build=x86_64-unknown-linux-gnu --prefix=${TOP}/sysroot --with-extrapath=${TOP}/buildroot/output/staging/usr --with-extrapath_lib=${TOP}/buildroot/output/target/usr/lib --with-extrapath_include=${TOP}/buildroot/output/staging/usr/include || print_error_msg "configure gst-pluging-renderer" 
		make -j8 && make install || print_error_msg "make gst-plugins-renderer"
		cd ${TOP}

		cd ${TOP}/gst-plugins-scaler
		./autogen.sh || print_autogen_fail_msg gst-plugins-scaler
		./configure --target=${cross_compile} --host=${cross_compile} --build=x86_64-unknown-linux-gnu --prefix=${TOP}/sysroot --with-extrapath=${TOP}/buildroot/output/staging/usr --with-extrapath_lib=${TOP}/buildroot/output/target/usr/lib --with-extrapath_include=${TOP}/buildroot/output/staging/usr/include || print_error_msg "configure gst-pluging-scaler" 
		make -j8 && make install || print_error_msg "make gst-plugins-scaler"
		cd ${TOP}

		cd ${TOP}/gst-plugins-camera-s5p6818
		# test -f Makefile && make install || make -f Makefile.cross install || echo "You must build buildroot before build gst-plugins-camera-s5p6818"
		./autogen.sh || print_autogen_fail_msg gst-plugins-camera-s5p6818
		./configure --target=${cross_compile} --host=${cross_compile} --build=x86_64-unknown-linux-gnu --prefix=${TOP}/sysroot --with-extrapath=${TOP}/buildroot/output/staging/usr --with-extrapath_lib=${TOP}/buildroot/output/target/usr/lib --with-extrapath_include=${TOP}/buildroot/output/staging/usr/include || print_error_msg "configure gst-pluging-renderer" 
		make -j8 && make install || print_error_msg "make gst-plugins-camera-s5p6818"
		cd ${TOP}

		export GST_SYSROOT=${TOP}/buildroot/output/staging
		export GST_CFLAGS="-I$GST_SYSROOT/usr/include -I$GST_SYSROOT/usr/include/gstreamer-1.0 -I$GST_SYSROOT/usr/include/glib-2.0 -I$GST_SYSROOT/usr/lib/glib-2.0/include"
		export GST_LIBS="-L$GST_SYSROOT/output/target/usr/lib -L$GST_SYSROOT/lib --sysroot=$GST_SYSROOT"

		cd ${TOP}/gst-plugins-video-enc
		./autogen.sh || print_autogen_fail_msg gst-plugins-video-enc
		./configure --target=${cross_compile} --host=${cross_compile} --build=x86_64-unknown-linux-gnu --prefix=${TOP}/sysroot || print_error_msg "make gst-plugins-video-enc"
		make -j8 && make install || print_error_msg "make gst-plugins-video-enc"
		cd ${TOP}

		cd ${TOP}/gst-plugins-video-dec
		./autogen.sh || print_autogen_fail_msg gst-plugins-video-dec
		./configure --target=${cross_compile} --host=${cross_compile} --build=x86_64-unknown-linux-gnu --prefix=${TOP}/sysroot || print_error_msg "make gst-plugins-video-dec"
		make -j8 && make install || print_error_msg "make gst-plugins-video-dec"
		cd ${TOP}

		cd ${TOP}/gst-plugins-video-sink
		./autogen.sh || print_autogen_fail_msg gst-plugins-video-sink
		./configure --target=${cross_compile} --host=${cross_compile} --build=x86_64-unknown-linux-gnu --prefix=${TOP}/sysroot || print_error_msg "make gst-plugins-video-sink"
		make -j8 && make install || print_error_msg "make gst-plugins-video-sink"
		cd ${TOP}
	fi
}

function build_buildroot()
{
	if [ ${BUILD_BUILDROOT} == "true" ] || [ ${BUILD_HWTEST} == "true" ]; then
		echo ""
		echo "================================================="
		echo "build buildroot"
		echo "================================================="

		cd ${TOP}/buildroot

		if [ "${CHIP_NAME}" == "s5p6818" ]; then
			make artik710_defconfig
		else
			make artik530_defconfig
		fi
		make

		cd ${TOP}
	fi
}

function build_hwtest()
{
	if [ ${BUILD_HWTEST} == "true" ]; then
		echo ""
		echo "================================================="
		echo "build hwtest"
		echo "================================================="

		cd ${TOP}/artik-hw-test

		make clean
		make CROSSNAME=$(get_cross_compile_prefix)-

		cd ${TOP}
	fi
}

function make_ext4()
{
	local result_dir=${1}
	local board_name=${2}
	local partition_name=${3}
	local partition_size=${4}

	PATH=${TOP}/tools-artik7/bin:$PATH \
		&& ${TOP}/tools-artik7/script/mkuserimg.sh -s ${result_dir}/${partition_name} \
		${result_dir}/${partition_name}.img ext4 ${partition_name} ${partition_size}
}

function make_2ndboot_for_sd()
{
	local result_dir=${1}
	local bl1_source=
	local file_name=
	if [ "${CHIP_NAME}" == "s5p6818" ]; then
		bl1_source=bl1-artik7
		file_name=${BOARD_PURENAME}-sd-32.txt
	else
		bl1_source=bl1-artik530
		file_name=${BOARD_PURENAME}-sd.txt
	fi
	local chip_name=$(echo -n ${CHIP_NAME} | awk '{print toupper($0)}')
	local nsih=${bl1_source}/reference-nsih/${file_name}
	tools-artik7/bin/BOOT_BINGEN -c ${chip_name} -t 2ndboot -n ${nsih} \
		-i ${result_dir}/bl1-${BOARD_PURENAME}.bin \
		-o ${result_dir}/bl1-sdboot.bin \
		-l 0xffff0000 -e 0xffff0000
}

function make_3rdboot_for_sd()
{
	local result_dir=${1}
	local bl1_source=
	local file_name=
	local inout_image=

	if [ "${CHIP_NAME}" == "s5p6818" ]; then
		bl1_source=bl1-artik7
		file_name=${BOARD_PURENAME}-sd-32.txt
		inout_image=singleimage
	else
		bl1_source=bl1-artik530
		file_name=${BOARD_PURENAME}-sd.txt
		inout_image=u-boot
	fi

	local chip_name=$(echo -n ${CHIP_NAME} | awk '{print toupper($0)}')
	local nsih=${bl1_source}/reference-nsih/${file_name}

	local load_addr=
	local jump_addr=
	if [ "${CHIP_NAME}" == "s5p6818" ]; then
		case "${MEM_SIZE}" in
			512)  load_addr=0x5fc00000; jump_addr=0x5fe00000 ;;
			1024) load_addr=0x7fc00000; jump_addr=0x7fe00000 ;;
			2048) load_addr=0xbfc00000; jump_addr=0xbfe00000 ;;
		esac
	else
		load_addr=0x43c00000
		jump_addr=0x43c00000
	fi

	tools-artik7/bin/BOOT_BINGEN -c ${chip_name} -t 3rdboot -n ${nsih} \
		-i ${result_dir}/${inout_image}.bin \
		-o ${result_dir}/singleimage-sdboot.bin \
		-l ${load_addr} -e ${jump_addr}
}

function make_2ndboot_for_emmc()
{
	local result_dir=${1}
	local bl1_source=
	local file_name=
	if [ "${CHIP_NAME}" == "s5p6818" ]; then
		bl1_source=bl1-artik7
		file_name=${BOARD_PURENAME}-emmc-32.txt
	else
		bl1_source=bl1-artik530
		file_name=${BOARD_PURENAME}-emmc.txt
	fi
	local chip_name=$(echo -n ${CHIP_NAME} | awk '{print toupper($0)}')
	local nsih=${bl1_source}/reference-nsih/${file_name}
	tools-artik7/bin/BOOT_BINGEN -c ${chip_name} -t 2ndboot -n ${nsih} \
		-i ${result_dir}/bl1-${BOARD_PURENAME}.bin \
		-o ${result_dir}/bl1-emmcboot.bin \
		-l 0xffff0000 -e 0xffff0000
}

function make_3rdboot_for_emmc()
{
	local result_dir=${1}
	local bl1_source=
	local file_name=
	local inout_image=

	if [ "${CHIP_NAME}" == "s5p6818" ]; then
		bl1_source=bl1-artik7
		file_name=${BOARD_PURENAME}-emmc-32.txt
		inout_image=singleimage
	else
		bl1_source=bl1-artik530
		file_name=${BOARD_PURENAME}-emmc.txt
		inout_image=u-boot
	fi

	local chip_name=$(echo -n ${CHIP_NAME} | awk '{print toupper($0)}')
	local nsih=${bl1_source}/reference-nsih/${file_name}

	local load_addr=
	local jump_addr=
	if [ "${CHIP_NAME}" == "s5p6818" ]; then
		case "${MEM_SIZE}" in
			512)  load_addr=0x5fc00000; jump_addr=0x5fe00000 ;;
			1024) load_addr=0x7fc00000; jump_addr=0x7fe00000 ;;
			2048) load_addr=0xbfc00000; jump_addr=0xbfe00000 ;;
		esac
	else
		load_addr=0x43c00000
		jump_addr=0x43c00000
	fi

	tools-artik7/bin/BOOT_BINGEN -c ${chip_name} -t 3rdboot -n ${nsih} \
		-i ${result_dir}/${inout_image}.bin \
		-o ${result_dir}/singleimage-emmcboot.bin \
		-l ${load_addr} -e ${jump_addr}
}

function copy_buildroot_exclusive()
{
	local src=${1}
	local compare=${2}
	local dest=${3}

	mkdir -p ${dest}/bin
	mkdir -p ${dest}/sbin
	mkdir -p ${dest}/lib

	for f in $(ls ${src}/bin); do
		if [ ! -d ${src}/bin/$f ]; then
			find_result=$(find ${compare} -name ${f})
			if [ "x" == "x${find_result}" ]; then
				cp -a ${src}/bin/${f} ${dest}/bin
			fi
		fi
	done

	for f in $(ls ${src}/sbin); do
		if [ ! -d ${src}/sbin/$f ]; then
			find_result=$(find ${compare} -name ${f})
			if [ "x" == "x${find_result}" ]; then
				cp -a ${src}/sbin/${f} ${dest}/sbin
			fi
		fi
	done

	for f in $(ls ${src}/lib); do
		if [ -d ${src}/lib/$f ]; then
			cp -a ${src}/lib/${f} ${dest}/lib
		else
			find_result=$(find ${compare} -name ${f})
			if [ "x" == "x${find_result}" ]; then
				cp -a ${src}/lib/${f} ${dest}/lib
			fi
		fi
	done
	rm -f ${dest}/lib/*.a

	# cp -a ${src}/share ${dest}
}

function release_info()
{
	local result_dir=$1

	local upper_model=$(echo -n ${BOARD_PREFIX} | awk '{print toupper($0)}')

	sed -i "s/RELEASE_VERSION=/RELEASE_VERSION=${RELEASE_VERSION}/" ${result_dir}/artik_release
	sed -i "s/RELEASE_DATE=/RELEASE_DATE=${RELEASE_DATE}/" ${result_dir}/artik_release
	sed -i "s/RELEASE_UBOOT=/RELEASE_UBOOT=${UBOOT_VERSION}/" ${result_dir}/artik_release
	sed -i "s/RELEASE_KERNEL=/RELEASE_KERNEL=${KERNEL_VERSION}/" ${result_dir}/artik_release
	sed -i "s/MODEL=/MODEL=${upper_model}/" ${result_dir}/artik_release
}

function post_process()
{
	echo ""
	echo "================================================="
	echo "post process"
	echo "================================================="

	local result_dir=$RESULT_DIR
	[ "$result_dir" == "" ] && result_dir=${TOP}/result-${BOARD_NAME}
	test -d ${result_dir} || mkdir -p ${result_dir}

	[ "$RELEASE_DATE" == "" ] && RELEASE_DATE=`date +"%Y%m%d.%H%M%S"`

	local bl1_source=
	local load_addr=
	if [ "${CHIP_NAME}" == "s5p6818" ]; then
		bl1_source=bl1-artik7
		load_addr=0x40080000
	else
		bl1_source=bl1-artik530
		load_addr=0x40008000
	fi
	cp ${TOP}/${bl1_source}/out/bl1-${BOARD_PURENAME}.bin ${result_dir}

	if [ "${ARM_ARCH}" == "arm64" ]; then
		cp ${TOP}/optee_build/result/singleimage.bin ${result_dir}
	else
		cp ${TOP}/u-boot-artik7/u-boot.bin ${result_dir}
	fi

	cp ${TOP}/tools-artik7/partmap/partmap_emmc.txt ${result_dir}
	cp ${TOP}/u-boot-artik7/params*.bin ${result_dir}

	make_2ndboot_for_sd ${result_dir}
	make_3rdboot_for_sd ${result_dir}
	make_2ndboot_for_emmc ${result_dir}
	make_3rdboot_for_emmc ${result_dir}

	mkdir -p ${result_dir}/boot
	${TOP}/u-boot-artik7/tools/mkimage -A ${ARM_ARCH} -O linux -T kernel -C none -a ${load_addr} -e ${load_addr} -n 'linux-4.1' -d ${TOP}/linux-artik7/arch/${ARM_ARCH}/boot/Image ${result_dir}/boot/uImage

	if [ "${ARM_ARCH}" == "arm64" ]; then
		if [ ${BOARD_NAME} == ${BOARD_PURENAME} ]; then
			cp ${TOP}/linux-artik7/arch/${ARM_ARCH}/boot/dts/nexell/${CHIP_NAME}-${BOARD_NAME}.dtb ${result_dir}/boot/
		else
			cp ${TOP}/linux-artik7/arch/${ARM_ARCH}/boot/dts/nexell/${CHIP_NAME}-${BOARD_PREFIX}-${BOARD_PURENAME}*.dtb ${result_dir}/boot/
		fi
	else
		if [ ${CHIP_NAME} == ${BOARD_PREFIX} ]; then
			cp ${TOP}/linux-artik7/arch/${ARM_ARCH}/boot/dts/${CHIP_NAME}-${BOARD_PURENAME}.dtb ${result_dir}/boot/
		else
			cp ${TOP}/linux-artik7/arch/${ARM_ARCH}/boot/dts/${CHIP_NAME}-${BOARD_PREFIX}-${BOARD_PURENAME}*.dtb ${result_dir}/boot/
		fi
	fi

	local root_dir=
	if [ "${ARM_ARCH}" == "arm64" ]; then
		root_dir=${TOP}/tools-artik7/root-arm64
	else
		root_dir=${TOP}/tools-artik7/root-arm
	fi

	cp -a ${TOP}/sysroot/lib/* ${root_dir}/usr/lib
	cp -a ${TOP}/sysroot/bin/* ${root_dir}/usr/bin
	cp -rf ${TOP}/sysroot/etc/ ${root_dir}/

	if [ "${ARM_ARCH}" == "arm64" ]; then
		cp -a ${TOP}/optee_client/out/export/bin/tee-supplicant ${root_dir}/usr/bin
		cp -a ${TOP}/optee_client/out/export/lib/* ${root_dir}/usr/lib

		sudo rm -rf ${root_dir}/lib/optee_armtz
		mkdir -p ${root_dir}/lib/optee_armtz
		cd ${TOP}/optee_test/out/ta
		find . -name "*.ta" -exec cp {} ${root_dir}/lib/optee_armtz \;
		cd ${TOP}
		chmod 444 ${root_dir}/lib/optee_armtz/*.ta

		cp ${TOP}/optee_test/out/xtest/xtest ${root_dir}/usr/bin
	fi

	# TODO : fail to boot to initrd made by mkinitramfs.sh
	# ${TOP}/tools-artik7/script/mkinitramfs.sh ${root_dir} ${result_dir}/boot
	# use ramdisk
	cd ${TOP}/tools-artik7
	local basename_rootdir=$(basename ${root_dir})
	./script/mkramdisk.sh ${basename_rootdir} 16
	cd ${TOP}
	mv ${TOP}/tools-artik7/*.img.gz ${result_dir}/boot/ramdisk.gz

	${TOP}/tools-artik7/bin/make_ext4fs -b 4096 -L boot \
		-l ${BOOT_PARTITION_SIZE} ${result_dir}/boot.img \
		${result_dir}/boot/

	mkdir -p ${result_dir}/modules
	rm -rf ${result_dir}/modules/*
	pushd ${TOP}/linux-artik7
	local cross_compile=$(get_cross_compile_prefix)-
	make ARCH=${ARM_ARCH} modules_install CROSS_COMPILE=${cross_compile} INSTALL_MOD_PATH=${result_dir}/modules INSTALL_MOD_STRIP=1
	popd

	if [ "${ARM_ARCH}" == "arm64" ]; then
		cp -a ${TOP}/optee_linuxdriver/armtz/*.ko ${result_dir}/modules/lib/modules/
		cp -a ${TOP}/optee_linuxdriver/core/*.ko ${result_dir}/modules/lib/modules/
	fi

	${TOP}/tools-artik7/bin/make_ext4fs -b 4096 -L modules \
		-l ${MODULES_PATITION_SIZE} ${result_dir}/modules.img \
		${result_dir}/modules/lib/modules/

	mkdir -p ${result_dir}/rootfs
	if [ ${BUILD_BUILDROOT} == "true" ]; then
		copy_buildroot_exclusive ${TOP}/buildroot/output/target/usr ${root_dir} ${result_dir}/rootfs
		cp -a ${TOP}/sysroot/lib/gstreamer-1.0/libgst* ${result_dir}/rootfs/lib/gstreamer-1.0 || echo "failed"
	fi
	if [ ${BUILD_HWTEST} == "true" ]; then
		rm -rf ${result_dir}/rootfs/*
	fi
	make_ext4 ${result_dir} ${BOARD_NAME} rootfs ${ROOT_PARTITION_SIZE}

	if [ ${BUILD_HWTEST} == "true" ]; then
		test -d ${result_dir}/rootfs-hwtest && rm -rf ${result_dir}/rootfs-hwtest
		mkdir -p ${result_dir}/rootfs-hwtest
		tar xvf ${TOP}/buildroot/output/images/rootfs.tar -C ${result_dir}/rootfs-hwtest
		cp -a ${result_dir}/rootfs-hwtest/lib/* ${result_dir}/rootfs-hwtest/usr/lib
		cp -a ${TOP}/artik-hw-test/bin/* ${result_dir}/rootfs-hwtest/usr/bin
	fi

	cp ${TOP}/tools-artik7/prebuilt/artik_release ${result_dir}/
	release_info ${result_dir}
}

parse_args $@
print_args
check_board_name ${BOARD_NAME}
get_board_prefix
parse_config $CONFIG_DIR/${BOARD_NAME}.cfg
setup_toolchain
if [ "${CHECK_BRANCH}" == "true" ]; then
	check_all_branch
fi
build_bl1
build_uboot
if [ "${ARM_ARCH}" == "arm64" ]; then
	build_optee
fi
build_kernel
if [ "${ARM_ARCH}" == "arm64" ]; then
	build_optee_module
fi
build_buildroot
build_hwtest
build_user
post_process
