a = [1,2,3,4,3,4,5,6,7]
for item in a:
    if a.count(item)>1:
        print(f'{item} is not unique')
    else:
        print(f'{item} is unique')
