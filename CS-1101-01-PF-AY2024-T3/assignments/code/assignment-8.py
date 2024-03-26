def invert_dictionary(original_dict):
    """
    Function to invert a dictionary where keys become values and values become keys.
    Args:
        original_dict (dict): The original dictionary to be inverted.
    Returns:
        dict: The inverted dictionary.
    """
    inverted_dict = {}
    for key, values in original_dict.items():
        for value in values:
            if value in inverted_dict:
                inverted_dict[value].append(key)
            else:
                inverted_dict[value] = [key]
    return inverted_dict

def read_students_file(file_name):
    """
    Function to read student data from a file and return it as a dictionary.
    Args:
        file_name (str): The name of the file to read from.
    Returns:
        dict: A dictionary containing student names as keys and their courses as values.
    """
    students_dict = {}
    try:
        with open(file_name, 'r') as file:
            for line in file:
                parts = line.strip().split(':')
                student = parts[0].strip()
                courses = [course.strip() for course in parts[1].split(',')]
                students_dict[student] = courses
    except FileNotFoundError:
        print(f"Error: File '{file_name}' not found.")
    except Exception as e:
        print(f"An error occurred while reading the file '{file_name}': {e}")
    return students_dict

def write_inverted_dict_to_file(inverted_dict, file_name):
    """
    Function to write an inverted dictionary to a file.
    Args:
        inverted_dict (dict): The inverted dictionary to be written to the file.
        file_name (str): The name of the file to write to.
    """
    try:
        with open(file_name, 'w') as file:
            for key, values in inverted_dict.items():
                file.write(key + ': ' + ', '.join(values) + '\n')
    except Exception as e:
        print(f"An error occurred while writing to the file '{file_name}': {e}")

# Read from students.txt
students_dict = read_students_file('students.txt')

# Invert the dictionary
inverted_dict = invert_dictionary(students_dict)

# Write the inverted dictionary to another file
write_inverted_dict_to_file(inverted_dict, 'inverted_students.txt')

# Display original and inverted files to the screen
print("Original students.txt:")
try:
    with open('students.txt', 'r') as file:
        print(file.read())
except FileNotFoundError:
    print("Error: Original students file not found.")

print("\nInverted inverted_students.txt:")
try:
    with open('inverted_students.txt', 'r') as file:
        print(file.read())
except FileNotFoundError:
    print("Error: Inverted students file not found.")
