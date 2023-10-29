import os
import shutil

from_dir="C:/Users/DELL/Downloads/c102_from"
to_dir="C:/Users/DELL/Downloads/c102_too"

listFiles=os.listdir(from_dir)
#print(listFiles)

for fileName in listFiles:
    name, ext = os.path.splitext(fileName)
    #print(name)
    #print(ext)
    if ext=='':
        continue
    if ext in ['.png','.gif','.jfif','.jpg','.jpeg']:
        path1 = from_dir + '/' + fileName
        path2 =  to_dir + '/' + "imageFiles"
        path3 =  to_dir + '/' + "imageFiles" + '/' + fileName

    if os.path.exists(path2):
        print("moving to path2")  
        shutil.move(path1,path2) 

    else :
        os.makedirs(path2)
        print("moving to path3")  
        shutil.move(path1,path3)  



