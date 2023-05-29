a = {'a':1,'b':3,'c':4}
b = {'b':8,'d':8,'c':10}
result = {}
for item in a.keys():
    if item in b.keys():
        result[item] = a[item]+b[item]
    else:
        result[item] = a[item]
for item in b.keys():
    if item not in result.keys():
        result[item] = b[item]
print(result)
