#!/bin/bash

#cut and copy white island camera images (like WIWR20140204033002UTC.jpg) to another folder once a jpg image placed in the directory

image_dir='/home/volcano/programs/white_island_lake_level_by_image'
analysis_dir=$image_dir'/image_manual'

inotifywait -m -e create --format '%f' $image_dir | while read file
do
	if [[ $file =~ jpg ]]
	then
		if [[ $file =~ WIWR ]]
		then
			sleep 5
   			#echo $file
			name=${file#WIWR}
			new_name=${name:0:8}_${name:8:13}

			#make image for manual analysis
			convert $file -crop '500x300+400+400' $analysis_dir/$new_name
			\rm $file
		fi
	fi
done
