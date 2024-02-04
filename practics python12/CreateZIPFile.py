from zipfile import *
f=ZipFile("files.zip",'w',ZIP_DEFLATED)
f.write("cricketers.text")
f.write("heroes.text")
f.write("social.text")
f.close()
print("files.zip file created successfully")