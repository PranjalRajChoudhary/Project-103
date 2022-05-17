import os
import shutil

path = input("Enter the directory to be operated :- ")
operation = input("Enter the operation to be done e.g move,delete,copy :- ")

root,ext = os.path.splitext(path)
print(root,ext)

if(operation == "delete"):
    if(os.path.exists(path)):
        if(ext == ''):
            for roots,dirs,files in os.walk(path):
                for file in files:
                    file_path = os.path.join(path,file)
                    os.remove(file_path)
                
                for dir in dirs:
                    dir_path = os.path.join(path,dir)
                    shutil.rmtree(dir_path)
        else:
            os.remove(path)

elif(operation == "copy"):
    if(os.path.exists(path)):
        destination = input("Enter the destination :- ")
        if(ext == ''):
         for roots,dirs,files in os.walk(path):
             for file in files:
                 shutil.copy(path+'/'+file,destination+'/')
        else:
             shutil.copy(path,destination+'/') 
             
elif(operation == "move"):
    print("Hi")
    if(os.path.exists(path)):
        print("hi")
        destination = input("Enter the destination :- ")
        if(ext == ''):
         for roots,dirs,files in os.walk(path):
             for file in files:
                 shutil.move(path+'/'+file,destination+'/')
        else:
             shutil.move(path,destination+'/')    

            
        

