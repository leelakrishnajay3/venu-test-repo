#!/bin/bash
LDTFile=/d/Ricoh/LDTFiles
if [ -d $LDTFile ]
then
 cd $LDTFile
 for i in `ls *ldt`
 do
 LDTSIZE=`ls -l $i|awk '{print $5}'`  
 if [ $LDTSIZE -gt 256000 ]
 then
 echo "$i:$LDTSIZE bytes" >> $LDTFile/files.txt
 fi
 done
 fi