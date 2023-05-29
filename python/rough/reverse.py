# # num = int(input("give any number"))
# # print(num) 
# # rev =0
# # while(num>0):
# #     rem = num%10
# #     num = num//10
# #     rev = rev*10+rem
# # print(rev)
# for i in range(5,0,-1):
#     print(i*' * ',end='\n')


# print("how are you?")
# for i in range(5,0):
#     print("hello")

def add5(function):
    def wrapper():
        func = function()
        func = func+5
        return func
    return wrapper
    
def add10(function):
    def wrapper():
        func = function()
        func = func+10
        return func
    return wrapper
    
@add10
@add5
def show0():
    return 13

print(show0())
