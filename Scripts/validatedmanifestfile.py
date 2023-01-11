import pandas as pd
import csv
import subprocess
import sys
ar_lst=list(sys.argv)
arg_manifestfile_path=ar_lst[1]
# seperator for the current csv file is ",".
# check whether all the iputs are provided by the user
with open(arg_manifestfile_path) as csvfile:
    csvReader = csv.reader(csvfile, delimiter=',')
    for row in csvReader:
        if len(row)<5:
            print (row)
            sys.exit("provide proper values seprated by commas")
df = pd.read_csv(arg_manifestfile_path)
print (df)
#data cleaning.
df = df.dropna(how='all')
#handling of mandatory values in the csv file.
mask1 = df[df['Path'].isnull()]
mask2 = df[df['Type'].isnull()]
mask3 = df[df['AppShortName'].isnull()]
if not mask1.empty:
    print (mask1)
    sys.exit("value of the path should be provided")
elif not mask2.empty:
    print (mask2)
    sys.exit("Type of the file should be provided")
elif not mask3.empty:
    print (mask2)
    sys.exit("AppShortName of the file should be provided")
else :
    print (" the mandatory values i.e Path, Type, Appshortname  are provided")
# handling of schemeas 
s_df = df.loc[df['Type'] == 'SQLSCRIPT']
mask4 = s_df[s_df['Schema'].isnull()]
if not mask4.empty:
    print (mask4)
    sys.exit ("Schema for the given sql file should be provided")
print ("hello")
# Sequencing of the files 
df = df.sort_values(by=['Sequence'], ascending=True )
print (df)
df.to_csv('deployment.csv',index=False)

# output = subprocess.call(['createzip.sh'])
# print(output)