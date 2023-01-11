#!/bin/bash 
# The variables in this script are
# 1. deploymentfile - This is the input file provided by developer
# 2. gitcheckout_path - This is git checkout path
# 3. source_path  - This is source files path provided by developer in csv file
# 4. COPY_PATH  - This is sourcefile temporary copy path
deploymentfile=$1
gitcheckout_path=$2 
COPY_PATH=$3 
source_path=`cat $deploymentfile | awk -F',' '{ print $1 }'| awk 'NR!=1'`
#check all the files are present or missing in the source path w.r.to deployment.csv file
for sourcefile in $source_path 
do  
cd $gitcheckout_path/src/ 
if [ -e $sourcefile ]; 
then 
echo "file is exist in the path:$sourcefile" >> $COPY_PATH/existing_files.log
else
echo "file mentioned in deployment.csv is missing in the path: $sourcefile" >> $COPY_PATH/missing_files.log
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
# copy all the existing files from source path to copy path directory
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
 echo "$sourcefile:$LDTSIZE bytes" >> $COPY_PATH/ldtexcesssize.log
 ldtexcesssize=true
 else 
 echo "$sourcefile:$LDTSIZE bytes" >> $COPY_PATH/ldtefile.log
 fi
 done
 fi
 if [ $ldtexcesssize ];
then
echo "Script is stopped, please check the ldt files in ldtexcesssize.log in the path $COPY_PATH"
exit 1
else
echo "ldt file size check is successfull, continue for file size check."  
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
echo "$sourcefile:$FILESIZE bytes" >> $COPY_PATH/files.log 
else  
echo "$sourcefile:$FILESIZE bytes" >> $COPY_PATH/files_zerosize.log 
filesizeiszero=true
fi 
done 
fi
if [ $filesizeiszero ];
then
echo "Script is stopped, please check the zero sized files in files_zerosize.log in the path $COPY_PATH"
exit 1
else
echo "file check is successfully done and start the archiving of the files."  
fi


