a = ['ex1','ex2','ex3']
b = ['ex2','ex3','ex5']
c = ['ex4','ex6','ex7']
a = set(a)
b = set(b)
c = set(c)
print((a.intersection(b))-c)