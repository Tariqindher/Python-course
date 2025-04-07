# What is a Function?
# A function is a group of statements that perform a specific task when called.
# Functions allow reusability and modularity in a program.

# Types of Functions in Python:

# 1. Built-in Functions – Predefined in Python (e.g., print(), len(), sum(), etc.)
# Example:
print(len("Hello"))  

# 2. User-defined Functions – Functions created by the programmer.
# Example:'
#Defining a Function
#A function is defined using the def keyword.

#Syntax:

def function_name(parameters):
    """Optional docstring"""
    # Function body
    return   # (Optional)


def greet():
    print("Hello, Welcome to Python!")

greet()  # Calling the function

# 3. Lambda Functions – Anonymous (one-line) functions.
# Syntax
# lambda arguments: expression
# Example:
square = lambda x: x * x
print(square(5))  


#Multiple with arguments
add = lambda a, b: a + b
print(add(3, 7))

# 4. Recursive Functions – Functions that call themselves.
# Example: Factorial using recursion
def factorial(n):
    if n == 1:
        return 1
    return n * factorial(n - 1)

print(factorial(5))  # Output: 120


#Functions with Parameter
def add(a, b):
    return a + b

result = add(5, 10)
print("Sum:", result)

#Function with default parameter
#If no value is provided for a parameter, a default value is used.
def greet(name="Guest"):
    print(f"Hello, {name}!")

greet("Tariq")
greet()  # Uses default value

#Keyword Arguments (kwargs)
#Python allows calling functions with named arguments.
def student(name, age):
    print(f"Name: {name}, Age: {age}")

student(age=20, name="Ali")  # Order doesn't matter


#Arbitrary Arguments (*args and **kwargs)
#Sometimes, the number of arguments is unknown.

#Using *args (Non-keyword arguments)
def total_marks(*marks):
    return sum(marks)

print(total_marks(80, 90, 85, 88))

#Using **kwargs (Keyword arguments)
#Used for passing multiple named arguments.
def student_info(**details):
    for key, value in details.items():
        print(f"{key}: {value}")

student_info(name="Tariq", age=22, course="Python")

#Return Statement
#The return statement is used to return a value from a function.
def square(num):
    return num * num

print(square(5)) 


#Scope and Lifetime of Variables
#There are two types of variable scope:

#Local Scope – Defined inside a function, accessible only within that function.
#Global Scope – Defined outside a function, accessible anywhere in the program.


x = 10  # Global variable

def my_function():
    x = 5  # Local variable
    print("Inside function:", x)

my_function()
print("Outside function:", x)


# Function with pass Statement
# If you want to define a function but not implement it yet, use pass.
def todo():
    pass  # Placeholder for future implementation

#Nested Function
def outer_function():
    def inner_function():
        print("I am inside the inner function!")
    inner_function()

outer_function()


#Function with Global Keyword
# The global keyword allows modifying global variables inside a function.
x = 5

def modify():
    global x
    x = 10

modify()
print(x)

# Function with nonlocal Keyword
# The nonlocal keyword modifies a variable in the outer function.
def outer():
    x = "Outer"

    def inner():
        nonlocal x
        x = "Inner"

    inner()
    print(x)  # Output: Inner

outer()


# Function Annotations
# Annotations specify the expected type of parameters and return values.
def add(a: int, b: int) -> int:
    return a + b

# Function Aliasing
# Functions can be assigned to another name.
def greet():
    print("Hello!")

welcome = greet
welcome() 

#Function as Argument
# Functions can be passed as arguments to other functions.
def greet():
    return "Hello"

def display_message(func):
    print(func())

display_message(greet)

# Function as Return Value
# A function can return another function.
def outer():
    def inner():
        print("Hello from inner function!")
    return inner

func = outer()
func()

#Generator Functions (yield)
#A generator function returns an iterator using yield.

def my_generator():
    yield 1
    yield 2
    yield 3

gen = my_generator()
print(next(gen)) 
print(next(gen))


#Decorators
#Decorators modify a function’s behavior.
def decorator(func):
    def wrapper():
        print("Before function execution")
        func()
        print("After function execution")
    return wrapper
@decorator
def hello():
    print("Hello, world!")

hello()


