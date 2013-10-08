#!/bin/bash
PD=$(date +%s)
SEQ=$(echo $1 | sed -e "s/%0[0-9]d/\*/g")
FD=$(echo $1 | cut -d_ -f1)
mkdir $FD
mv $SEQ $FD
cd $FD
avconv -f image2 -r 3 -i $1 -r 24 ${PD}.avi
