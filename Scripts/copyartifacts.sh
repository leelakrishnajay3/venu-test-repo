#!/bin/bash 
# The variables in this script are
# 1. Workspace - This is the name of workspace
# 2. gitcheckout_path - This is git checkout path
# 3. source_path  - This is source path provided by developer in csv file
# 4. COPY_PATH  - This is sourcefile copy path
# 5. artifacts_path - This is artifact storage path
#validating csv file
deploymentfile=$1
gitcheckout_path=$2 
COPY_PATH=$3 
source_path=`cat $deploymentfile | awk -F',' '{ print $1 }'| awk 'NR!=1'`
#artifacts_path=/d/RICOH/Artifacts
#check all the files are present or missing in the source path w.r.to deployment.csv file
for sourcefile in $source_path 
do  
cd $gitcheckout_path/src/ 
if [ -e $sourcefile ]; 
then 
echo "file is exist in the path:$sourcefile" >> $COPY_PATH/available_files.txt
else
echo "file mentioned in deployment.csv is missing in the path: $sourcefile" >> $COPY_PATH/missing_files.txt
missing=true
fi 
done 
if [ $missing ];
then
echo "Script is stopped, please check the missing files in missing_files.txt in the path $COPY_PATH "
exit 1
else
echo "file check is successfully done and start the copying files."  
fi
# copy all the presented files from source path to copy path directory
for sourcefile in $source_path 
do  
cd $gitcheckout_path/src/
echo "$sourcefile"
cp -r $sourcefile $COPY_PATH
done
#check if ldt file size is greaterthan 250kb, please stop the execution of the script.
if [ -d $COPY_PATH ]
then
 cd $COPY_PATH
 for sourcefile in `ls *ldt`
 do
 LDTSIZE=`ls -l $sourcefile |awk '{print $5}'`  
 if [ $LDTSIZE -gt 256000 ]
 then
 echo "$i:$LDTSIZE bytes" >> $LDTFile/files.txt
 fi
 done
 fi
#check if file size is less than zero, please stop the execution of the script. 
if [ -d $COPY_PATH ] 
then 
cd $COPY_PATH 
for sourcefile in `ls *` 
do 
FILESIZE=`ls -l $sourcefile | awk '{print $5}'`   
if [ $FILESIZE -gt 0 ] 
then 
echo "$sourcefile:$FILESIZE bytes" >> $COPY_PATH/size_files.txt 
else  
echo "$sourcefile:$FILESIZE bytes" >> $COPY_PATH/zerosize_files.txt 
filesizeiszero=true
fi 
done 
fi
 if [ $filesizeiszero ];
then
echo "Script is stopped, please check the zero sized files in zerosize_files.txt in the path $COPY_PATH "
exit 1
else
echo "file check is successfully done and start the archiving of the files."  
fi
#copy the manifest file into copy_path
#echo "copy the file deployment.csv into copy_path"
#cp -r $deploymentfile $COPY_PATH
#if [ $?=0 ];
#then
#echo "manifest file copied successfully."
#else 
#echo "manifest file copied is failed."
#fi
# package the files in zip or tar file format. 
#if [ -d $COPY_PATH ];
#then
#cd $COPY_PATH/
#tar -cvf CHR1234.tar .
#if [ $?=0 ];
#then
#echo "tar or zip file created successfully."
#else 
#echo "tar or zip file creation is failed."
#fi
#fi
# copy the tar file to local artifacts path. 
# Note - This local path for storing artifact, for remote storing, we need to change the script with SSH, SCP commands. 
#if [ -d $COPY_PATH ];
#then
#cd $COPY_PATH/
#cp -r CHR1234.tar $artifacts_path/
#if [ $?=0 ];
#then
#echo "tar or zip file copied successfully."
#else 
#echo "tar or zip file copy is failed."
