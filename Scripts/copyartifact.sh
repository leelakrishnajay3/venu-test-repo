#!/bin/bash 
# The variables in this script are
# 1. COPY_PATH  - This is sourcefile copy path
# 2. artifacts_path - This is artifact storage path
COPY_PATH=$1 
#copy the tar file to local artifacts path. 
# Note - This local path for storing artifact, for remote storing, we need to change the script with SSH, SCP commands. 
if [ -d $COPY_PATH ];
then
cd $COPY_PATH/
cp -r CHR1234.tar $artifacts_path/
if [ $?=0 ];
then
echo "tar or zip file copied successfully."
else 
echo "tar or zip file copy is failed."