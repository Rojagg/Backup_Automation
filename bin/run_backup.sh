#!/bin/bash


devices=$(jq -r "keys_unsorted[]" "$PWD/../devices.json")

for n in $devices
do
	dirPath=$PWD/../backups/$n
	mkdir -p $dirPath
	mkdir -p $dirPath/archive
done

python3 $PWD/../scripts/backup.py


