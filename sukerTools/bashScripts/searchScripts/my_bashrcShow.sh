#!/bin/bash


echo "alias crash_w7='crash --rawdump DDRCS0.BIN@0x0-0x20000000,DDRCS1.BIN@0x20000000-0x20000000 -p 4096 -m phys_base=0x00000 --no_panic --smp vmlinux'"
echo "alias c8c8='quota -us choonghyun.jeon'"
echo "alias c8='python ~/sukerScripts/main.py'"
echo "alias _grms=find . -name "*\.mk" -o -name "*\.sh" -print0 | xargs -0 grep --color -n $1"
echo "alias _grxml=find . -type f -name "*\.xml" -print0 | xargs -0 git grep --color -n $1"
echo "alias _gra=find . -name '*' -print0 | xargs -0 grep --color -n $1"
echo "alias cd=cd $1 && pwd > ~/pwd"
echo "alias _gl=git log --pretty=oneline --grep $1"
echo "alias _gs=git show $1"
echo "alias fnf=find . -name $1 -type f"
echo "alias fnd=find . ! \( -path './out' -prune \) -name $1 -type d"
echo "alias _grc=find . -type f -name "*\.c" -print0 | xargs -0 grep --color -n $1"
