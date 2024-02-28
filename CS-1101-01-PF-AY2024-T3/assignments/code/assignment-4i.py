def hypotenuse(a, b):
    """Calculates the length of the hypotenuse of a right triangle given the lengths of the other two legs as arguments.

    Args:
        a: The length of the first leg (in any unit of measurement).
        b: The length of the second leg (in the same unit of measurement as a).

    Returns:
        The length of the hypotenuse (in the same unit of measurement as a and b).
    """

    # Calculate the square of each leg.
    a_squared = a**2
    b_squared = b**2

    # Calculate the hypotenuse using the Pythagorean theorem.
    hypotenuse = (a_squared + b_squared)**0.5

    # Return the length of the hypotenuse.
    return hypotenuse


# Real-world examples:

# Calculating the length of a ladder needed to reach a certain height on a wall
ladder_height = 10
ladder_distance_from_wall = 6

# Calculate the length of the ladder using the Pythagorean theorem.
ladder_length = hypotenuse(ladder_height, ladder_distance_from_wall)

# Output: 11.66

# Calculating the distance between two points on a map
point_a_x_coordinate = 30
point_a_y_coordinate = 40
point_b_x_coordinate = 50
point_b_y_coordinate = 60

# Calculate the distance between the two points using the Pythagorean theorem.
distance_between_points = hypotenuse((point_a_x_coordinate - point_b_x_coordinate), (point_a_y_coordinate - point_b_y_coordinate))

# Output: 28.28

# Test the function code with different arguments.
print(hypotenuse(3, 4))  # Output: 5.0
print(hypotenuse(12, 5))  # Output: 13.0
print(hypotenuse(6, 8))  # Output: 10.0