import commands

def read_line(path, start=1, length=1):
    newScriptFile = open("build_uboot.sh", "wt")
    for line in (commands.getoutput('head -%s %s | tail -%s' % ((start + (length -1)), path, length))).split("\n"):
        print line
        newScriptFile.write(line+"\n")

read_line("build.sh", 59, 51)
