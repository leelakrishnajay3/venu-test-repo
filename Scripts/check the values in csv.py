#import csv
#with open('CHR12345.csv') as file:
#    reader = csv.reader(file)
#    for row in reader:
#        print(row)
   csvfile = read.csv(CHR12345,sep = ",", fileEncoding = "utf-16")

 if (ncol(csvfile)==1){
   csvfile = read.csv(file,sep = " ", fileEncoding = "utf-16")
}       