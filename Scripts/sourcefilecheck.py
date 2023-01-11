import pandas as pd
  
# read specific columns of csv file using Pandas
source_path = pd.read_csv("sequence_validation.csv", usecols = ['Path'])
print (source_path)
#for sourcefile in source_path:
#print (sourcefile)