#!/bin/bash

#if manual_measures.csv is modified, run plotting script

image_dir='/home/volcano/programs/white_island_lake_level_by_image'
analysis_dir=$image_dir'/image_manual'
web_dir='/var/www/html/volcanoes/whiteis'

inotifywait -m -e create --format '%f' $analysis_dir | while read file
do
	if [[ $file == 'manual_measures.csv' ]]
	then
   		$image_dir/lake_height_vs_time.py $analysis_dir/manual_measures.csv $image_dir/lake_height.png
		scp $image_dir/lake_height.png $web_dir
		\rm $analysis_dir/manual_measures.csv
	fi
done
