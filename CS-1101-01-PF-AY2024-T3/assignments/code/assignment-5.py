def display_left(s, n):
    """Display n characters from the left."""
    print("Left", n, "characters:", s[:n])

def count_vowels(s):
    """Count the number of vowels."""
    vowels = "aeiouAEIOU"
    count = 0
    for char in s:
        if char in vowels:
            count += 1
    print("Number of vowels:", count)

def reverse_string(s):
    """Reverse the string."""
    print("Reversed string:", s[::-1])

def main():
    # Input string
    string = "Irfan Manzoor"

    # Displaying the input string
    print("Input string:", string)

    # Asking user for the number of characters to display from the left
    n = int(input("Enter the number of characters to display from the left: "))

    # Display n characters from the left
    display_left(string, n)

    # Count the number of vowels
    count_vowels(string)

    # Reverse the string
    reverse_string(string)

if __name__ == "__main__":
    main()