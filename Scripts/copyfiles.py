import pandas as pd
import os
import shutil
df=pd.read_csv(r"deployment.csv")
for i,row in df.iterrows():
    if row["Type"] == "JAVA":
        custom_application=row["AppShortName"]
        source=row["Path"]
        sourcefile=source.split("/")[-1]
        os.chdir("C:/Oracle-pipeline/Artifacts")
        destination_files=os.listdir()
        for javafile in destination_files:
            if javafile == sourcefile:
                path="C:/Oracle-pipeline/"+custom_application+"_TOP/java"
                shutil.copy(javafile, path)
    elif row["Type"] == "REPORT":
        custom_application=row["AppShortName"]
        source=row["Path"]
        sourcefile=source.split("/")[-1]
        os.chdir("C:/Oracle-pipeline/Artifacts")
        destination_files=os.listdir()
        for rdffile in destination_files:
            if rdffile == sourcefile:
                path="C:/Oracle-pipeline/"+custom_application+"_TOP/REPORT"
                shutil.copy(rdffile, path)
    elif row["Type"] == "FORMS":
        custom_application=row["AppShortName"]
        source=row["Path"]
        sourcefile=source.split("/")[-1]
        os.chdir("D:\Ricoh\svn2github\Artifacts")
        destination_files=os.listdir()
        for formfile in destination_files:
            if formfile == sourcefile:
                path="D:\\Ricoh\\svn2github\\"+custom_application+"_TOP\\FORMS"
                shutil.copy(formfile, path)            
    elif row["Type"] == "SQLSCRIPT":
        custom_application=row["AppShortName"]
        source=row["Path"]
        sourcefile=source.split("/")[-1]
        os.chdir("D:\Ricoh\svn2github\Artifacts")
        destination_files=os.listdir()
        for SQLfile in destination_files:
            if SQLfile == sourcefile:
                path="D:\\Ricoh\\svn2github\\"+custom_application+"_TOP\\SQLSCRIPT"
                shutil.copy(SQLfile, path)            
    elif row["Type"] == "JSP":
        custom_application=row["AppShortName"]
        source=row["Path"]
        sourcefile=source.split("/")[-1]
        os.chdir("D:\Ricoh\svn2github\Artifacts")
        destination_files=os.listdir()
        for JSPfile in destination_files:
            if JSPfile == sourcefile:
                path="D:\\Ricoh\\svn2github\\"+custom_application+"_TOP\\JSP"
                shutil.copy(JSPfile, path)            
    elif row["Type"] == "JAVASCRIPT":
        custom_application=row["AppShortName"]
        source=row["Path"]
        sourcefile=source.split("/")[-1]
        os.chdir("D:\Ricoh\svn2github\Artifacts")
        destination_files=os.listdir()
        for javascriptfile in destination_files:
            if javascriptfile == sourcefile:
                path="D:\\Ricoh\\svn2github\\"+custom_application+"_TOP\\JAVASCRIPT"
                shutil.copy(javascriptfile, path)    
    elif row["Type"] == "STYLESHEET":
        custom_application=row["AppShortName"]
        source=row["Path"]
        sourcefile=source.split("/")[-1]
        os.chdir("D:\Ricoh\svn2github\Artifacts")
        destination_files=os.listdir()
        for stylesheetfile in destination_files:
            if stylesheetfile == sourcefile:
                path="D:\\Ricoh\\svn2github\\"+custom_application+"_TOP\\STYLESHEET"
                shutil.copy(stylesheetfile, path)

                                 
        
                

        

    

        
        




            



                

          



            
            
