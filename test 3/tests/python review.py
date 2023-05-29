# print('python string slices')
# a = 'ashik'
# print(a[:-2])  #prints  ash
# print(a[-1:-2])  #prints  nothing
# print(a[-1:-2:-1])  #prints  k
# print(a[-1:-6])  #prints  nothing
# print(a[-1:-6:-1])  #prints  kihsa
# print(a[-1:-7:-1])  #prints  kihsa
# print(a[1:7:1])  #prints  shik

# print('python string methods')
# print('Note: All string methods returns new values. They do not change the original string.')
# a = 'Hello man! AshikG'
# print(a.upper())  #HELLO MAN! ASHIKG
# print(a.lower())  #hello man! ashikg
# print(a.capitalize())  #Hello man! ashikg
# b = ' how are you   '
# print(b.strip('s')) #will work
# print(b.strip())
# print(a.casefold()) #same like lower() but more aggressinve 
# print(a.center(30)) #center aligned like total 30 steps  #      Hello man! AshikG       
# print(a.center(30,'*'))  # ******Hello man! AshikG*******
c = 'Hello man! this is AshikG'

print(c.count('i'))
print(c.index('l')) #2
print(c.index('man')) #6
print(c.find('man')) #6
print(c.title()) #Hello Man! This Is Ashikg
print(c.capitalize()) #Hello man! this is ashikg
print([x for x in reversed(c)])
print(''.join([x for x in reversed(c)]))
d = ['da','bdsfad',' cdd']
print(''.join(d))
print(max(d,key=len)) # bdsfad
print(max(d)) # da
print('Note: All string methods returns new values. They do not change the original string.')
# print(c.__reversed__()) # AttributeError: 'str' object has no attribute '__reversed__'
# print(c.reverse()) # AttributeError: 'str' object has no attribute 'reverse'

a = [3,5,5,6,4,5,'hi','ashik','g']
a.remove(5)
a.remove('hi')
# a.sort()  # TypeError: '<' not supported between instances of 'str' and 'int'
b = [5,6,73,3,4,6,3,44,4,9]
b.sort()
print(b)
b.reverse()
print(b)
# a.remove(5,3)  #TypeError: list.remove() takes exactly one argument (2 given)


