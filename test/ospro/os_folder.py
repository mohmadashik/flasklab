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
### listing the files in the current directory .
# '***********************'
# files = os.scandir('.')
# print('the files are ')
# print(files)
# for file in files:
#     print(file.name)
# print('reading the files in current directory')
# ### when you have traversed through the os.scandir('.') 
# ### you can't do it again. because all have been traversed.
# ### you need to create the file traverser once again 
# files = os.scandir('.')
# for file in files:
#     f = open(file.name,'r')
#     print('first file is ',file.name)
#     print(f.read())
#     f.close()
# '***********************'

### listing only directories in the current directory 
# # '***********************'

# dirs = os.listdir('.')
# ## print(dirs)  #not what we wanted! prints all folders including files too
# ###
# items = dirs
# print('printing only directory names')
# for item in dirs:
#     if os.path.isdir(item):
#         print(item)
# '***********************'

### creating a folder 
# # '***********************'
# print('before creation ')
# print(os.listdir('.'))
# os.mkdir('created_dir')
# print('after creation ')
# print(os.listdir('.'))

# # '***********************'

### deleting a folder 
# # '***********************'
os.mkdir('example_dir')
print('before deletion ')
print(os.listdir('.'))
# os.rmdir('example_dir') ### working fine
print('after deletion ')
print(os.listdir('.'))

# # '***********************'



