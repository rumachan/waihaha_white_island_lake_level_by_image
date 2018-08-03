#!/bin/bash

#input format 20160215_002002UTC
#output format 2016-02-15T00:20:02Z

for file in `ls 2*.jpg`
do 
	f=${file%.*}
	dt=$f
	d=`echo $dt | sed 's/UTC//' | awk 'BEGIN{FS="_"}{print $1}'`
	t=`echo $dt | sed 's/UTC//' | awk 'BEGIN{FS="_"}{print $2}'`

	newd=`date -d $d +%Y-%m-%d`
	newt=`echo $t | awk 'BEGIN{FS=""}{printf("T%s%s:%s%s:%s%sZ\n", $1,$2,$3,$4,$5,$6)}'`

	echo $newd$newt
done
