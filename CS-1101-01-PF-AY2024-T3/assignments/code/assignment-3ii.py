def main():
    # Prompt the user for the numerator and convert it to a float
    numerator = float(input("Enter the numerator: "))
    
    # Prompt the user for the denominator and convert it to a float
    denominator = float(input("Enter the denominator: "))

    # Check if the denominator is zero
    if denominator == 0:
        # Handle division by zero error and inform the user
        print("Error: Division by zero is not allowed.")
    else:
        # Perform the division operation if the denominator is not zero
        result = numerator / denominator
        
        # Display the result to the user
        print(f"Result of {numerator} / {denominator} is {result}")

if __name__ == "__main__":
    # Call the main function when the script is executed
    main()