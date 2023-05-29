a='abcDefAc'
for i in a:
    if ord(i) in range(97,97+26):
        print('small letter ',i)
    else:
        print('big letter ',i)
