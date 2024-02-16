# Function Definition:
def print_circum(radius):
    # Manually define the value of π (pi) rounded to five decimal places:
    pi = 3.14159
    
    # Calculate the circumference using the formula: 2πr
    circumference = 2 * pi * radius
    
    # Print the result with a formatted message displaying the radius and circumference with five decimal places:
    print(f"The circumference of a circle with radius {radius} is {circumference:.5f}")

# Function Calls:
# Calculate and print the circumferences for circles with different radii:
print_circum(5.0)
print_circum(7.5)
print_circum(10.2)