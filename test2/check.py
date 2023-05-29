# a=[10,20,30,40]
# b=a.copy()
# a.append(50)
# b.append(50)
# b.append(60)
# print(a)
# print(b)
# result 
"""
[10, 20, 30, 40, 50]
[10, 20, 30, 40, 50, 60]
"""

# 2nd

# a=[10,20,30,40]
# b=a
# a.append(50)
# b.append(50)
# b.append(60)
# print(a)
# print(b)
"""
result 
[10, 20, 30, 40, 50, 50, 60]
[10, 20, 30, 40, 50, 50, 60]
"""

# #3rd
# a=[10,20,[30,50],40]
# b=a
# a[2].append(50)
# b[2].append(50)
# b[2].append(60)
# print(a)
# print(b)

"""
result 
[10, 20, [30, 50, 50, 50, 60], 40]
[10, 20, [30, 50, 50, 50, 60], 40]
"""

#4th

# a=[10,20,[30,50],40]
# b=a.copy()
# a[2].append(50)
# b[2].append(50)
# b[2].append(60)
# print(a)
# print(b)

"""
result 
[10, 20, [30, 50, 50, 50, 60], 40]
[10, 20, [30, 50, 50, 50, 60], 40]
"""

#5th
# import copy
# a=[10,20,[30,50],40]
# b=copy.copy(a)  #same for b=a,b=a.copy()
# a[2].append(50)
# b[2].append(50)
# b[2].append(60)
# print(a)
# print(b)
"""
result 
[10, 20, [30, 50, 50, 50, 60], 40]
[10, 20, [30, 50, 50, 50, 60], 40]
"""

# #6th
# import copy
# a=[10,20,[30,50],40]
# b=copy.deepcopy(a)  
# a[2].append(50)
# b[2].append(50)
# b[2].append(60)
# print(a)
# print(b)

"""
result 
[10, 20, [30, 50, 50], 40]
[10, 20, [30, 50, 50, 60], 40]
"""


#7th
# import copy
# a=[10,20,[30,50],40]
# b=copy.deepcopy(a)  
# a[2].append(50)
# # b[2].append(50)
# # b[2].append(60)
# print(a)
# print(b)

"""
result 
[10, 20, [30, 50, 50], 40]
[10, 20, [30, 50], 40]
"""

#8th
import copy
a=[10,20,[30,50],40]
b=copy.copy(a)  #same for b=a,b=a.copy()
a.append(50)
b.append(50)
b.append(60)
print(a)
print(b)
"""
result 
[10, 20, [30, 50], 40, 50]
[10, 20, [30, 50], 40, 50, 60]
"""
