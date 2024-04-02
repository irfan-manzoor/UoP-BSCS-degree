def invert_dictionary(input_dict):
    # Initialize an empty dictionary to store the inverted data
    inverted_dict = {}
    # Iterate through each student and their courses in the input dictionary
    for student, courses in input_dict.items():
        # For each course, add the student to the list of students in the inverted dictionary
        for course in courses:
            # If the course is not already in the inverted dictionary, create a new entry with the student's name
            # Otherwise, append the student's name to the existing list of students for that course
            inverted_dict.setdefault(course, []).append(student)
    return inverted_dict

def print_as_table(dictionary, title):
    # Print the title of the table
    print(f"{title}:")
    # Print a horizontal line to separate the title from the table
    print("-" * 25)
    # Iterate through each key-value pair in the dictionary and print them in tabular format
    for key, value in dictionary.items():
        # Print the key followed by a colon and the list of values separated by commas
        print(f"{key}:".ljust(10), ', '.join(value))

def main():
    # Sample input dictionary
    students_courses = {
        'Arfan': ['Math', 'CS', 'DSA'],
        'Adnan': ['CS', 'DSA', 'Programming'],
        'Aadil': ['Math', 'Programming', 'UI/UX']
    }

    # Printing original dictionary
    print_as_table(students_courses, "Original Dictionary")
    print()

    # Inverting the dictionary
    inverted_courses_students = invert_dictionary(students_courses)

    # Printing inverted dictionary
    print_as_table(inverted_courses_students, "Inverted Dictionary")

if __name__ == "__main__":
    main()
