# decorators start with @ mark, like @decorator_name
# decorators are functions that take other functions as arguments
# decorators are used to modify the behavior of other functions. 
# decorators are used to modify the behavior of other functions.

def hello(func):
    def wrapper(*args, **kwargs):
        print("Hello")      #this is gonna print as is
        func(*args,**kwargs)              #this is where the decorator is applied
        print("Nice to meet You!")    #this is gonna print as is
    return wrapper

@hello #name of the decorator that we created above
def hi(*name):
    print(name,end=", ") #gk: print function takes end and sep as arguments too

# hello(hi()) 

# prints Hello, Hi, Goodbye where Hello and Goodbye are the decorator
# and Hi is the function that is being decorated.

# def bye():
#     print("Bye")

# a = hello(bye) # this way we dont have to use the @ symbol
# a()

# now the actual useful exapmle of decorators where we can pass the arguments to the actual function
# hi("Maheshwor") # prints Hello, Maheshwor, Nice to meet You!

a = hello(hi("Maheshwor"))
hello(hi())

