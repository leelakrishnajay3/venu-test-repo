#!/bin/bash
JAVA_SRC=/d/Ricoh/svn2github/CU1234/JAVA
JAVA_TOP=/d/Ricoh/JAVA
DATA_TOP=/d/Ricoh/svn2github/sourcevalidation.csv
source=`cat $DATA_TOP | awk -F',' '{ print $1 }' | cut -d '/' -f8-10 | sed -n /CU/p | awk -F'/' '{ print $3 }'`
for i in $source
do
   echo $i
   #cp $JAVA_SRC/$i $JAVA_TOP/
   #javac $JAVA_TOP/*.java
done


