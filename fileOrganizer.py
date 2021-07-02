import os
import shutil
#writing the name of directory here that needs to get sorted and providing the path
path = input("enter the name of the directory to be sorted:-")
#this is will create a properly organized list with all the file names that are in the directory
list_of_files = os.listdir(path)
#this will go through each and every file 
for file in list_of_files:
    name , ext = os.path.splittext(file)
    #this is going to store the ext type
    ext = ext[1:]
    #this forces the next iteration if it is the directory
    if ext == '':
        continue
    #this will move the files to the directory where the name 'ext' already exists
    if os.path.exists(path+'/'+ext):
        shutil.move(path+'/'+file, path+'/'+ext+'/'+file)
        #this will create a new directory if directory does not already exist
        else:
            os.makedirs(path+'/'+ext)
            shutil.move(path+'/'+file, path+'/'+ext+'/'+file)
    