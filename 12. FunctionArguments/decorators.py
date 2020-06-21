#
# 1. Functions are ojects

def add_five(num):
    print(num + 5)
    
add_five(2)

print()
print( add_five ) # will print <function add_five at 0x107e2d440> since add_five is an object. Thus, you can pass it around like an object.

#
# 2 Functions within Function

print()
def add_five(num):
    def add_two(num):
        return num +2
    num_plus_two = add_two(num)
    print(num_plus_two + 3)
    
add_five(10) # will print 15

# uncomment the next line to test the error
#add_two(7) # will create an error when print since add_two is defined inside and only inside add_five. YOu can'y call it outside the function.

#
# 3. Returning functions from functions

def get_math_function(operation): # + or -
    def add(n1, n2):
        return n1 + n2
    def sub(n1, n2):
        return n1 - n2
    if operation == '+':
        return add
    elif operation == '-':
        return sub

add_function = get_math_function('+')
print()
print( add_function )
print()
print( add_function(4,6))

#
# 4, Decorating a function
print()
def title_decorator(print_name_function):
    def wrapper(): # using a wrapper function
        print("Dr:")
        print_name_function()
    return wrapper

@title_decorator
def print_my_name():
    print("Ovando")
 
@title_decorator   
def print_joes_name():
    print("Joe") # can call print_joes_name to print Professor Joe.

print_my_name()  #used to test print_my_name() - can also be used with @title_decorator

# the following was commented out because you can simply use @title_decorator to do the same thing.
#decorated_function = title_decorator(print_my_name)
#decorated_function()

#print_my_name("shelby") # will get an error, see next example

#
# 6 decorators with Parameters (some how misses 5 since the tutor went over everything really fast)
print()
def title_decorator(print_name_function):
    def wrapper(*args, **kwargs): # using a wrapper function
        print("Dr:")
        print_name_function(*args, **kwargs)
    return wrapper

@title_decorator
def print_my_name(name, age):
    print(name + " you are " + str(age)) 
    
print_my_name("shelby", 50) # this should now work, and you can pass in as many arguments as you want.