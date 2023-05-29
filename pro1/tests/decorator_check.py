from functools import wraps
def age_check(func):
    wraps(func)
    def check_age_is_18(*args,**kwargs):
        age = args[0]
        if age <19:
            print('you are not eligible kiddo!')
            return 
        func(*args,**kwargs)
    return check_age_is_18

@age_check
def welcome(age):
    print(f'Welcome, to Grand Plaza')

age = int(input('Hi hero , enter your age! '))
welcome(age)

