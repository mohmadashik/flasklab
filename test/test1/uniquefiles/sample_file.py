import os 
print('before creation')
print(os.listdir())
filename  = 'ex.mp3'
f = None
if not os.path.exists(filename):
    new_filename =filename
else:
    i = 1 
    while os.path.exists(f'{filename.split(".")[0]}{i}.{filename.split(".")[1]}'):
        i+=1
    new_filename = f'{filename.split(".")[0]}{i}.{filename.split(".")[1]}'
f = open(new_filename,'w')
f.write('sample text')
f.close()
print('after creation')
print(os.listdir())
