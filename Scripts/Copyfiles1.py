import pandas as pd
import os
import shutil
df=pd.read_csv(r"D:\Ricoh\svn2github\deployment1.csv")
for i,row in df.iterrows():
    if row["Type"] == "JAVA":
        source=row["Path"]
        sourcefile=source.split("/")[-1]
        destination_files=os.listdir("D:\Ricoh\svn2github\CU1234\src\JAVA")
        for javafile in sourcefile:
            if javafile == sourcefile:
                path="D:\Ricoh\CHR1234"
                shutil.copy(javafile, path)
    # elif row["Type"] == "SQLSCRIPT":
    #     source=row["Path"]
    #     sourcefile=source.split("/")[-1]
    #     destination_files=os.listdir("D:\Ricoh\svn2github\CU1234\src\SQL")
    #     for sqlfile in destination_files:
    #         print(sqlfile)
    #         if sqlfile == sourcefile:
    #             path="D:\Ricoh\CHR1234"
    #             shutil.copy(javafile, path)
    # elif row["Type"] == "JAVASCRIPT":
    #     source=row["Path"]
    #     sourcefile=source.split("/")[-1]
    #     destination_files=os.listdir("D:\Ricoh\svn2github\CU1234\src\JAVASCRIPT")
    #     for javascriptfile in destination_files:
    #         if javascriptfile == sourcefile:
    #             path="D:\Ricoh\CHR1234"
    #             shutil.copy(javascriptfile, path)
    # elif row["Type"] == "REPORTS":
    #     source=row["Path"]
    #     sourcefile=source.split("/")[-1]
    #     destination_files=os.listdir("D:\Ricoh\svn2github\CU1234\src\REPORTS")
    #     for reportfile in destination_files:
    #         if reportfile == sourcefile:
    #             path="D:\Ricoh\CHR1234"
    #             shutil.copy(reportfile, path)
    # # elif row["Type"] == "STYLESHEET":
    # #     source=row["Path"]
    # #     sourcefile=source.split("/")[-1]
    # #     destination_files=os.listdir("D:\Ricoh\svn2github\CU1234\src\STYLESHEET")
    # #     for stylesheetfile in destination_files:
    # #         if stylesheetfile == sourcefile:
    # #             path="D:\Ricoh\CHR1234"
    # #             shutil.copy(stylesheetfile, path)
    # elif row["Type"] == "FORMS":
    #     source=row["Path"]
    #     sourcefile=source.split("/")[-1]
    #     destination_files=os.listdir("D:\Ricoh\svn2github\CU1234\src\FORMS")
    #     for formfile in destination_files:
    #         if formfile == sourcefile:
    #             path="D:\Ricoh\CHR1234"
    #             shutil.copy(formfile, path)
    # elif row["Type"] == "JSP":
    #     source=row["Path"]
    #     sourcefile=source.split("/")[-1]
    #     destination_files=os.listdir("D:\Ricoh\svn2github\CU1234\src\JSP")
    #     for jspfile in destination_files:
    #         if jspfile == sourcefile:
    #             path="D:\Ricoh\CHR1234"
    #             shutil.copy(jspfile, path)                                    
    # else:
    #     print('No file is found')
