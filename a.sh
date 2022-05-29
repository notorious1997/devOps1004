#!/bin/bash

usage()
{
    echo "Program for uncompressing  tar, gzip, rar archives"
    echo "Allowed parametres: --help, --file, --input, --directory"
    echo "Examples:"
    echo "./uncompress.sh --file firstFile secondFile"
    echo "./uncompress.sh --input inputFile.txt"
    echo "./uncompress.sh --directory /home/"

}


uncompress_file()
{
    if [ -f $1 ]
    then
        temp1=`file $1 | cut -d: -f2 | grep tar`

            if [ "$temp1" != "" ]
                then
                    echo    "$1 is a tar archive, uncompressing..."
                    tar xf $1 > /dev/null
            fi

        temp1=`file $1 | cut -d: -f2 | grep RAR`

            if [ "$temp1" != "" ]
                then
                    echo    "$1 is a rar archive, uncompressing..."
                    unrar e $1 > /dev/null
            fi

        temp1=`file $1 | cut -d: -f2 | grep gzip`

            if [ "$temp1" != "" ]
                then
                    echo    "$1 is a gzip archive, uncompressing..."
                    tar xzf $1 > /dev/null

            fi


    else
    echo    "$1 is not a valid file!"
    fi
}

uncompress_dir()
{
    for file in "$1"/*
        do
            if [ -f $file ]
            then
            uncompress_file $file
            fi


            if [ -d $file ]
            then
            uncompress_dir $file
            fi


        done

}







if [ "$1" = "--help" ]
    then
    usage
    exit

fi

if test $# -lt 2
    then echo "What about parametres?" 1>&2
    exit 1
fi



param=$1;
shift;





if [ "$param" = "--file" ]
    then

        while [ $# -ne 0 ]
        do
            uncompress_file $1
            shift
        done
    exit
fi

if [ "$param" = "--input" ]
    then
        if [ -f $1 ]
            then
                while read line
                do
                    uncompress_file $line

                done < $1
            else
                echo "$1 is not a valid file"
        fi
    exit
fi


if [ "$param" = "--directory" ]
    then
        if [ -d $1 ]
            then
                uncompress_dir $1
            else
            echo    "$1 is not a valid directory"
        fi
    exit
fi


echo "wrong parametres!";