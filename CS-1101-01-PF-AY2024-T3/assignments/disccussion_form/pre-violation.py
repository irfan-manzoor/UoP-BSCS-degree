def calculate_average(numbers):
    # Preconditions: 'numbers' must be a non-empty list of numerical values
    if not numbers or not all(isinstance(num, (int, float)) for num in numbers):
        raise ValueError("Invalid input: 'numbers' must be a non-empty list of numerical values.")

    # Incorrect implementation: Summing the numbers instead of calculating the average
    total = sum(numbers)
    return total / len(numbers)

# Trying to calculate the average with an empty list, violating the precondition
result = calculate_average([])
print(result)