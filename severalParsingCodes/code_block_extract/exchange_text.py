# -*- coding: utf-8 -*-

replace_list = [["cd ${TOP}/u-boot-artik7","cd ${S}"]]

def replace_text(read_path, old, new) :
    import fileinput
    for line in fileinput.input(read_path, inplace = 1):
        print line.replace(old, new),


replace_text("build_uboot.sh", replace_list[0][0], replace_list[0][1])
