#!/bin/bash 
# The variables in this script are
# 1. deploymentfile - This is the input file provided by developer
# 2. source_path  - This is source files path provided by developer in csv file
deploymentfile=/d/RICOH/svn2github/deployment.csv
source_path=`cat $deploymentfile | awk -F',' '{ print $1 }'| awk 'NR!=1'|cut -d / -f2`
source_type=`cat $deploymentfile | awk -F',' '{ print $2 }'| awk 'NR!=1'`
for type in $source_type
do
#echo "$type"
case $type in
        "JAVA")
        for sourcefile in $source_path
        do
      #   appshortname=`cat $deploymentfile | awk -F',' '{ print $1,$3 }'| awk 'NR!=1' | grep "$sourcefile" | cut -d / -f2 | cut -d ' ' -f2`
          echo "$sourcefile"
      #   for custom_application in $appshortname
      #    do
      #    cp -r $sourcefile "$custom_application"_TOP/java/
      #    echo "copy $sourcefile is successfull to $custom_application"
      #    done
         done
           ;;
        esac
        done