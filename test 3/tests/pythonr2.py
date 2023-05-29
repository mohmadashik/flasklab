# #checking the decorator
# from functools import wraps
# def check_name(func):
#     @wraps(func)
#     def name_checking(*args,**kwargs):
#         name = args[0]
#         if name=='ashik':
#             print('wrong name given change the name')
#             return
#         func(*args,*kwargs)
#     return name_checking

# @check_name
# def print_the_name(name):
#     print('the name is ',name)

# input_name = input('give a name\n')
# print_the_name(input_name)

#filter usage 

# def check_even(a):
#     return True if a%2==0 else False
# arr = [1,2,3,4,5,6,7,8]
# print('filter returns a generator object')
# print(filter(check_even,arr))

# print([filter(check_even,arr)])

# print([x for x in filter(check_even,arr)])

# from functools import wraps
# def check_zero_division(func):
#     wraps(func)
#     def check_zero(*args,**kwargs):
#         x,y = args[0],args[1]
#         if y==0:
#             return "zero cannot be used as a divider"
#         else:
#             return func(x,y)
#     return check_zero

# @check_zero_division
# def divide(x,y):
#     return x/y

# a = int(input('give divident '))
# b = int(input('give divider '))
# print(divide(a,b))

from functools import wraps

def check_age(func):
    wraps(func)
    def valid_age(*args,**kwargs):
        age = args[0]
        # return "you are not eligible" if age<=17 else func(age) # this line is not showing the error message for 17 or below
        if age <18:
            print('you are not eligible from decorator function')
            return "you are not eligible"
        else:
            return func(age)
    return valid_age

@check_age
def print_age(age):
    print(f"your age is {age}")

your_age = int(input("give your age brother ")) 
print_age(your_age)





