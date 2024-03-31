# Function to count down from a positive number to zero
def countdown(n):
    if n <= 0:  # Base case: when n reaches zero or negative, print 'Blastoff!'
        print('Blastoff!')
    else:
        print(n)  # Print the current number
        countdown(n - 1)  # Recursively call countdown with n-1

# Function to count up from a negative number to zero
def countup(n):
    if n >= 0:  # Base case: when n reaches zero or positive, print 'Blastoff!'
        print('Blastoff!')
    else:
        print(n)  # Print the current number
        countup(n + 1)  # Recursively call countup with n+1

# Main function for user interaction
def main():
    number = int(input("Enter a number: "))  # Get user input as an integer
    
    if number > 0:
        countdown(number)  # If input is positive, call countdown
    elif number < 0:
        countup(number)  # If input is negative, call countup
    else:
        countdown(number)  # If input is zero, call countdown (arbitrarily chosen)

if __name__ == "__main__":
    main()  # Run the main function when the script is executed