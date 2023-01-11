import zipfile, os 
handle = zipfile.ZipFile('BUILDID.zip', 'w')
os.chdir('D:\RICOH-DEVOPSTEST\temp')
handle.write(x, compress_type = zipfile.ZIP_DEFLATED)
handle.close()
