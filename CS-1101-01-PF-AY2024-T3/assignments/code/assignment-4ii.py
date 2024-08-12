def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        result = 1
        for i in range(2, n + 1):
            result *= i
        return result

# Test cases
print(factorial(0))  # Output: 1
print(factorial(5))  # Output: 120
print(factorial(10)) # Output: 3628800