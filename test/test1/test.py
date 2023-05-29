class Check:
  def __init__(self):
    self.namer = 'checkobj'
  @staticmethod
  def checkname(name):
    if type(name)==str:
      return True
    else:
      return False
  def checker(self,name):
    if type(name)==str:
      return True
    else:
      return False
obj = Check()
print(obj.checker(name='ashikg'))
print(obj.checkname(name='ashik'))
















# a = [{"23":"4a3","a":"cd2"},'a1c2b','21ang','92c','451c',2]
# import pdb
# sum=0
# for i in a:
#     pdb.set_trace()
#     type_of_varialbe = type(i)
#     if type_of_varialbe == int:
#         sum+=i
#     elif type_of_varialbe == str:
#         for j in i:
#             if j in '0 1 2 3 4 5 6 7 8 9'.split():
#                 sum+=int(j)
#     elif type_of_varialbe == dict:
#         for n in i.keys():
#             for j in n:
#                 if j in '0 1 2 3 4 5 6 7 8 9'.split():
#                     sum+=int(j)
#         for j in i.values():
#             for j in n:
#                 if j in '0 1 2 3 4 5 6 7 8 9'.split():
#                     sum+=int(j)
# print(sum)

