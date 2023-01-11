import subprocess
import pandas as pd
import os
df_url=pd.read_excel(r"C:\Users\RDhania\Desktop\Module.xlsx")
mylist = df_url['Module_name'].tolist()
print(mylist)
for e in mylist:
    dir=(e.split("/"))[-1]
    #print(dir)
    e=e.replace(" ","%20")
    url=e
    os.system("svn checkout  --depth infinity "+url)
    os.chdir(dir)
    #print(url)
    lst_url=url.split('/')
    #print(lst_url)
    repoName=lst_url[4]+'_'+lst_url[-2]+'_'+lst_url[-1]
    repoName=repoName.replace("%20","")
    #print(repoName)
    file=".svn"
    #print(os.getcwd())
    os.system("echo " +file+" >> .gitignore")
    os.system("git init")
    os.system("git add .")
    msg='"'+lst_url[-1]+'COMMIT"'
    os.system("git commit -m "+msg)
    os.system("gh repo create "+repoName+" --private --source=. --remote=upstream")
    gitUrl="https://github.com/DSrinkudhania/"+repoName+".git"
    os.system("git remote add origin "+gitUrl)
    os.system("git push -u origin master")
    os.chdir("..")
    #print(os.getcwd())