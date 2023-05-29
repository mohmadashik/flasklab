n=0
a = ['ex.jpg','ex1.jpg','ex2.jpg','yes.mp3','yes2.mp3']
name = 'ex1.jpg'
for i in range(n,n+1):
    # if os.path.exists(f'{base_path}{file_name}-{i}.{file_ext}'):
    if name not in a:
        print(n,i,'if')    
else:
    n+=1
    print(n,i,'else')
