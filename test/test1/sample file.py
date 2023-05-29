import os 
i = 0 
filename  = 'sample.txt'
while os.path.exists(f'{filename.split(".")[0]}{i}{filename.split(".")[1]}'):
    i+=1
new_filename = f'{filename.split(".")[0]}{i}{filename.split(".")[1]}'
f = open(new_filename)
f.write('sample text')
f.close()
