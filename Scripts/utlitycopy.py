import pandas as pd
import os
import shutil
from zipfile import ZipFile
from zipfile import ZIP_DEFLATED
import glob

import sys
ar_lst=list(sys.argv)
arg_manifestfile_path=ar_lst[1]
arg_targetpath=ar_lst[2]
arg_source=ar_lst[3]


df=pd.read_csv(arg_manifestfile_path)
lst=df['Type']
dist_type=list(set(lst))
#print(dist_type)


targetpath=arg_targetpath
os.chdir(targetpath)
sdir=arg_source

def get_all_file_paths(directory):
  
    # initializing empty file paths list
    file_paths = []
  
    # crawling through directory and subdirectories
    for root, directories, files in os.walk(directory):
        for filename in files:
            # join the two strings in order to form the full filepath.
            filepath = os.path.join(root, filename)
            file_paths.append(filepath)
  
    # returning all file paths
    return file_paths

for i in dist_type:
    os.mkdir(i)
#print(os.getcwd())
#print(os.listdir())

os.chdir(sdir)
#print(os.getcwd())
for i,row in df.iterrows():
    if row["Type"] == "JAVA":
        sourcedir=sdir+"/"+str(row["Type"])
        os.chdir(sourcedir)
        source=row["Path"]
        sourcefile=source.split("/")[-1]
        path=targetpath+"/"+row["Type"]
        shutil.copy(sourcefile, path)
        os.chdir(sdir)
    elif row["Type"] == "REPORT":
        sourcedir=sdir+"/"+str(row["Type"])
        os.chdir(sourcedir)
        source=row["Path"]
        sourcefile=source.split("/")[-1]
        path=targetpath+"/"+row["Type"]
        shutil.copy(sourcefile, path)
        os.chdir(sdir)
    elif row["Type"] == "FORMS":
        sourcedir=sdir+"/"+str(row["Type"])
        os.chdir(sourcedir)
        source=row["Path"]
        sourcefile=source.split("/")[-1]
        path=targetpath+"/"+row["Type"]
        shutil.copy(sourcefile, path)
        os.chdir(sdir)
    elif row["Type"] == "SQL":
        sourcedir=sdir+"/"+str(row["Type"])
        os.chdir(sourcedir)
        source=row["Path"]
        sourcefile=source.split("/")[-1]
        path=targetpath+"/"+row["Type"]
        shutil.copy(sourcefile, path)
        os.chdir(sdir)
    elif row["Type"] == "JSP":
        sourcedir=sdir+"/"+str(row["Type"])
        os.chdir(sourcedir)
        source=row["Path"]
        sourcefile=source.split("/")[-1]
        path=targetpath+"/"+row["Type"]
        shutil.copy(sourcefile, path)
        os.chdir(sdir)
    elif row["Type"] == "JAVASCRIPT":
        sourcedir=sdir+"/"+str(row["Type"])
        os.chdir(sourcedir)
        source=row["Path"]
        sourcefile=source.split("/")[-1]
        path=targetpath+"/"+row["Type"]
        shutil.copy(sourcefile, path)
        os.chdir(sdir)
    elif row["Type"] == "STYLESHEET":
        sourcedir=sdir+"/"+str(row["Type"])
        os.chdir(sourcedir)
        source=row["Path"]
        sourcefile=source.split("/")[-1]
        path=targetpath+"/"+row["Type"]
        shutil.copy(sourcefile, path)
        os.chdir(sdir)
    else:
        print("file is not presnet")
os.chdir(targetpath)
#os.chdir("newtargetpath")
#os.system("zip filename.zip "+targetpath)


import shutil

shutil.make_archive('buildID', format='zip', root_dir=targetpath)