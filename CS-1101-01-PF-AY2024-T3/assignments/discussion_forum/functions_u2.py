# Example 1
def greet(name):  # 'name' is the parameter
    print("Hello, " + name + "!")

# "World" is the argument
greet("World")  # 'World' is the argument

# Example 2
# Calling the function with different kinds of arguments: a value, a variable, and an expression.

# Value argument
greet("Irfan")  # "Alice" is a value argument

# Variable argument
person = "Manzoor"
greet(person)  # 'person' is a variable argument

# Expression argument
greet("Hello" + " " + "Ahmad")  # "Hello" + " " + "Ahmad" is an expression argument

# Example 3
def my_function():
    # Local variable
    x = 10
    print("Inside the function:", x)

my_function()
# Trying to use the local variable 'x' outside the function
# This will cause an error since 'x' is not defined outside the function.
#print("Outside the function:", x)