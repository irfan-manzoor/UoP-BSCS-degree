# Example 1:
# Define a function that takes an argument
def greet(name):
    print("Hello,", name)

# Call the function with an argument
greet("Irfan")

# Explanation:
# In this example, the function `greet` takes one parameter, `name`. When we call the function `greet("Irfan")`, 
# "Irfan" is the argument passed to the function. The parameter `name` in the function definition acts as a placeholder 
# for the actual value provided when the function is called.

# Output Explanation:
# The output is "Hello, Irfan", which is the result of calling the function `greet` with the argument "Irfan".


# Example 2:
# Call the function from Example 1 with different kinds of arguments
value_arg = "Rayaan"
variable_arg = "Azlaan"
expression_arg = "Haadi"

greet(value_arg)                      # Call with a value argument
greet(variable_arg)                   # Call with a variable argument
greet(variable_arg + " and " + expression_arg)  # Call with an expression argument

# Explanation:
# Here, we call the `greet` function three times with different kinds of arguments:
# 1. `value_arg` is a value passed directly as an argument.
# 2. `variable_arg` is a variable whose value is passed as an argument.
# 3. `variable_arg + " and " + expression_arg` is an expression whose result is passed as an argument.

# Output Explanation:
# The outputs are "Hello, Rayaan", "Hello, Azlaan", and "Hello, Azlaan and Haadi", respectively.
# These outputs correspond to the results of calling the `greet` function with different arguments.


# Example 3:
# Construct a function with a local variable
def my_func():
    local_var = 42
    print("Inside the function:", local_var)

# Call the function
my_func()

# Try to use the local variable outside the function
print("Outside the function:", local_var)

# Explanation:
# In this example, `local_var` is a local variable defined within the `my_func` function. 
# Attempting to access `local_var` outside the function results in a NameError because 
# `local_var` is not defined in the global scope.

# Output Explanation:
# The output "Inside the function: 42" is produced by the `print` statement inside the function `my_func`,
# which prints the value of the local variable `local_var`. 
# The output "NameError: name 'local_var' is not defined" is a result of trying to access `local_var` 
# outside the function scope, which raises a NameError because `local_var` is not defined in the global scope.


# Example 4:
# Construct a function that takes an argument
def print_value(parameter):
    print("Parameter value:", parameter)

# Call the function
print_value(10)

# Attempt to use the parameter name outside the function
print("Outside the function:", parameter)

# Explanation:
# The function `print_value` takes a parameter named `parameter`. When called, `print_value(10)`, 
# `10` is passed as an argument and assigned to `parameter`. Attempting to access `parameter` outside 
# the function scope results in a NameError because `parameter` is a local variable within the function.

# Output Explanation:
# The output "Parameter value: 10" is produced by the `print` statement inside the function `print_value`,
# which prints the value of the parameter `parameter`. 
# The output "NameError: name 'parameter' is not defined" is a result of trying to access `parameter` 
# outside the function scope, which raises a NameError because `parameter` is not defined in the global scope.


# Example 5:
# Variable defined outside the function
var = "global"

# Construct a function with a local variable having the same name as the global variable
def my_function():
    var = "local"
    print("Inside the function:", var)

# Call the function
my_function()

# Print the global variable
print("Outside the function:", var)

# Explanation:
# Inside the function `my_function`, `var` is a local variable that shadows the global variable `var`.
# When accessing `var` inside the function, the local variable is used. Outside the function, 
# the global variable `var` retains its original value because the local variable's scope is limited to 
# the function block.

# Output Explanation:
# The output "Inside the function: local" is produced by the `print` statement inside the function `my_function`,
# which prints the value of the local variable `var`. 
# The output "Outside the function: global" is produced by the `print` statement outside the function,
# which prints the value of the global variable `var`.