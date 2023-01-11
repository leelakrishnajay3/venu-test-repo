import glob
import os
import pandas as pd
import shutil
df=pd.read_csv(r"D:\Ricoh\svn2github\manifestfile.csv")
for i,row in df.iterrows():
    if row["Type"] == "JAVA":     
        source=row["Path"]
        sourcefile=source.split("/")[-1]
        JAVA_PATH=source.split("/")[-2]
        JAVA=os.mkdir("D:/Ricoh/CHR1234/"+JAVA_PATH)
        for filename in glob.glob(pattern, recursive=True):
            if os.path.isfile(filename):
                path="D:\Ricoh\CHR1234"
                shutil.copy(filename, path)
            # else:
            #     print("file is not found")    
    elif row["Type"] == "FORMS":     
        source=row["Path"]
        formfile=source.split("/")[-1]
        pattern = "D:/Ricoh/svn2github/CU1234/src/FORMS/"+formfile
        for filename in glob.glob(pattern, recursive=True):
            if os.path.isfile(filename):
                path="D:\Ricoh\CHR1234"
                shutil.copy(filename, path)
    elif row["Type"] == "REPORT":     
        source=row["Path"]
        reportfile=source.split("/")[-1]
        pattern = "D:/Ricoh/svn2github/CU1234/src/REPORTS/"+reportfile
        for filename in glob.glob(pattern, recursive=True):
            if os.path.isfile(filename):
                path="D:\Ricoh\CHR1234"
                shutil.copy(filename, path)
    elif row["Type"] == "SQLSCRIPT":     
        source=row["Path"]
        sqlscriptfile=source.split("/")[1]
        pattern = "D:/Ricoh/svn2github/CU1234/src/SQL/"+sqlscriptfile
        for filename in glob.glob(pattern, recursive=True):
            if os.path.isfile(filename):
                path="D:\Ricoh\CHR1234"
                shutil.copy(filename, path)
    elif row["Type"] == "JAVASCRIPT":     
        source=row["Path"]
        javascriptfile=source.split("/")[-1]
        pattern = "D:/Ricoh/svn2github/CU1234/src/JAVASCRIPT/"+javascriptfile
        for filename in glob.glob(pattern, recursive=True):
            if os.path.isfile(filename):
                path="D:\Ricoh\CHR1234"
                shutil.copy(filename, path)
    elif row["Type"] == "JSP":     
        source=row["Path"]
        jspfile=source.split("/")[-1]
        pattern = "D:/Ricoh/svn2github/CU1234/src/JSP/"+jspfile
        for filename in glob.glob(pattern, recursive=True):
            if os.path.isfile(filename):
                path="D:\Ricoh\CHR1234"
                shutil.copy(filename, path) 
    elif row["Type"] == "STYLESHEET":     
        source=row["Path"]
        stylesheetfile=source.split("/")[-1]
        pattern = "D:/Ricoh/svn2github/CU1234/src/STYLESHEET/"+stylesheetfile
        for filename in glob.glob(pattern, recursive=True):
            if os.path.isfile(filename):
                path="D:\Ricoh\CHR1234"
                shutil.copy(filename, path)                                                              
    else:
        print("file is not found")   