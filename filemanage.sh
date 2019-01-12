#!/bin/bash
path="/media/pi/RaSegate/movie"
cd $path

# remove blank in folder name
find -name *\ * |
while read name
do
    na=$(echo $name | tr ' ' '_')
    mv "$name" $na
done 

# list media file
arr=()
function getdir(){
    for element in `ls $1`
    do
        dir_or_file=$1"/"$element
        if [ -d $dir_or_file ]
        then
            getdir $dir_or_file
        else
            arr+=($dir_or_file)
        fi
    done
}
for file in $path/*
do
    if [[ -d $file ]]
    then
        getdir $file
    fi
done

# move media file
for file in "${arr[@]}"
do
    if [ ${file##*.} == "mp4" ] || [ ${file##*.} == "mkv" ]
    then
        size=`ls -l $file | awk '{print $5}'`
        if [ $size -gt 1000000000 ]
        then
            name=`basename $file`
            mv $file $path/$name
        fi
    fi
done

# remove folder
for file in $path/*
do
    if [[ -d $file ]]
    then
        rm -rf $file
    fi
done