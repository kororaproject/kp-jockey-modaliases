#!/bin/sh
#
# Create modaliases for kmod packages
# Copyright (c) 2011, Hedayat Vatankhah <hedayat.fwd@gmail.com>
# Distributed under GPL version 3 or any later version
#

LATEST_KERNEL_VER=
EXCLUDE_KMOD_PKGS="kmod-xtables-addons"
NO_AKMOD_PKGS="kmod-staging"

OUTPUT_BASENAME=rpmfusion-modules
OUTPUT=${OUTPUT_BASENAME}.aliases
OUTPUT_DIR=modaliases-$(date +%F_%R)

mkdir $OUTPUT_DIR
cd $OUTPUT_DIR

echo "Downloading kmod packages..."
echo "================================================================="
yumdownloader "kmod*${LATEST_KERNEL_VER}*"

[ -e $OUTPUT ] && echo "Output file already exists: $OUTPUT" && exit 1

echo "Generating modalias files..."
echo "================================================================="

for kmodpkg in *.rpm; do
	PKGNAME="${kmodpkg%%-${LATEST_KERNEL_VER}*}"
	if [[ $EXCLUDE_KMOD_PKGS == *${PKGNAME}* ]]; then
		echo "Excluded kmod: $EXCLUDE_KMOD_PKGS"
		continue;
	fi

	rpmdev-extract "$kmodpkg" > /dev/null
	PKGDIR="${kmodpkg%.rpm}"
	KMODS="$(find "$PKGDIR" -name "*ko")"
        for kmod in $KMODS; do
		MODULE_NAME=$(basename $kmod)
		MODULE_NAME=${MODULE_NAME%.ko}
		modinfo $kmod | grep "alias:.*:" | sed "s|alias: *\(.*\)|alias \1 ${MODULE_NAME} ${PKGNAME}|" >> $OUTPUT
		modinfo $kmod | grep "alias:.*:" | sed "s|alias: *\(.*\)|alias \1 ${MODULE_NAME} ${PKGNAME}-PAE|" >> $OUTPUT_BASENAME-PAE.aliases

		if [[ $NO_AKMOD_PKGS == *${PKGNAME}* ]]; then
			AKMOD_PKGNAME=$PKGNAME
		else
			AKMOD_PKGNAME=a$PKGNAME
		fi
		modinfo $kmod | grep "alias:.*:" | sed "s|alias: *\(.*\)|alias \1 ${MODULE_NAME} ${AKMOD_PKGNAME}|" >> $OUTPUT_BASENAME-akmods.aliases
	done
	echo "Package: $PKGNAME"
	rm -rf "${PKGDIR}"
done

echo "Output files ready in $OUTPUT_DIR"
