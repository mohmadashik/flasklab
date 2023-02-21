import os
# print(os.path)
# print(os.name)
# print(os.curdir)
# print(os.sep)
# # os.sep = 'dl'   # no need to change! but we can change it
# # print(os.sep)   # changed os path separator, usually it is / or \\
# print(os.extsep)
# print(os.altsep)
# print(os.pathsep) # prints all functions in the module
# print(dir(os))
files = os.scandir('.')
print('the files are ')
print(files)
for file in files:
    print(file.name)
print('reading the files in current directory')
### when you have traversed through the os.scandir('.') 
### you can't do it again. because all have been traversed.
### you need to create the file traverser once again 
files = os.scandir('.')
for file in files:
    f = open(file.name,'r')
    print(f.read())
    f.close()