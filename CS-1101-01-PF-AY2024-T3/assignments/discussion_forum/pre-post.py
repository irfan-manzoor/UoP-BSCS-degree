def get_name():
    return 42  # Incorrect return type, expecting a string

# Incorrect usage, trying to concatenate an integer with a string
name = "Hello, " + get_name()
print(name)