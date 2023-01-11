#!/bin/bash
#copy the source file by validating sourcevalidation.csv file
deploymentfile=/d/Ricoh/svn2github/sourcevalidation.csv
gitcheckout_path=/d/Ricoh/svn2github/CU1234
COPY_PATH=/d/Ricoh/CHR1234
sequence=`cat $deploymentfile | awk -F',' '{ print $5 }'`
#app_shortname=`cat $Workspace | awk -F',' '{ print $3 }'`
for compilesequence in $sequence
do
if [ $compilesequence -gt 0 ]
then
#source_path=`cat $Workspace | awk -F',' '{ print $1,$5 }'| grep "$compilesequence" | cut -d ' ' -f1`
source_path=`cat $deploymentfile | awk -F',' '{ print $1,$5 }'| awk 'NR!=1' |awk NR='$compilesequence'| grep "$compilesequence" | cut -d ' ' -f1`
else 
source_path=`cat $deploymentfile | awk -F',' '{ print $1,$5 }'| cut -d ' ' -f1`
for sourcefile in $source_path
do 
echo $sourcefile
cd $gitcheckout_path/src/
if [ -f $sourcefile ]
then
echo $sourcefile
cp -r $sourcefile $COPY_PATH
echo "file is copied successfull:$sourcefile" >> $COPY_PATH/copied_files.txt
else 
echo "file mentioned in sourcevalidation.csv is missing: $sourcefile" >> $COPY_PATH/missing_files.txt
fi
done
fi
done
#check the file size is greater than 0
if [ -d $COPY_PATH ]
then
cd $COPY_PATH
for sourcefile in `ls *`
do
FILESIZE=`ls -l $sourcefile | awk '{print $5}'`  
if [ $FILESIZE -gt 0 ]
then
echo "$sourcefile:$FILESIZE bytes" >> $COPY_PATH/Size_files.txt
else 
echo "$sourcefile:$FILESIZE bytes" >> $COPY_PATH/zerosize_files.txt
rm -rf $sourcefile 
fi
done
fi


