#!/bin/bash

echo "Initiating XML Data Updater!"

#var find ./ -mtime -1 -ls


oIFS=$IFS
IFS=$'\n'
count=0
find ./ -mtime -1 -ls | while read -r i; do
  #echo $i
  if [ $count == 0 ]; then
   	echo 'escaping ROOT dir '$(echo $i | awk '{print $11}')
  	count=1
  	#echo $count
  	else
  		echo 'Updating files to HDFS'
  		file=$(echo $i | awk '{print $11}' | sed 's|.//||g' ) 
  		scp $file root@xmhdp-ch2-en01d.sys.comcast.net:/home/spatel493
  		echo $file 'uploaded'
  	fi
done
	
IFS=$oIFS