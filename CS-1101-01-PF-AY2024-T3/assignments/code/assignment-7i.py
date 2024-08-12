def invert_dictionary(original_dict):
    """
    Here we define a function called invert_dictionary that takes
    in a dictionary called original_dict as input. It creates an empty
    dictionary called inverted_dict to store the inverted mapping.
    The function then iterates over the key-value pairs in original_dict. 
    For each pair, it checks if the course is already present in inverted_dict.
    If not, it adds an empty list as the value for that course.
 
    Then it appends the student to the list of students for that course in
    inverted_dict. The loop breaks if the list of students for a course reaches
    a length of 3.
    
    In the end, the function returns the inverted_dict containing the inverted mapping.

    """
    inverted_dict = {}
    for students, courses in original_dict.items():
        for course in courses:
            # If course is not already in inverted dictionary, add it with an empty list
            if course not in inverted_dict:
                inverted_dict[course] = []
            # Append the student to the list of students for this course
            inverted_dict[course].append(students)
            # Break if each key has three different values
            if len(inverted_dict[course]) == 3:
                break
    return inverted_dict

def print_courses_and_students(courses):
    """
    Here we define a function called print_courses_and_students that takes 
    a dictionary courses as input. The function iterates over the key-value 
    pairs, where each key represents a course and each value is a list of 
    students enrolled in that course.
    
    For each course, the function prints the course name, followed by a list of 
    the enrolled students. The function uses f-strings to format the output.
    """
    for course, students in courses.items(): # Iterate over the key-value pairs
        print(f"Course: {course}")           # Print the course
        print("Students Enrolled:")
        for student in students:             # Print the list of students
            print(f"- {student}")            # Print each student
        print()

# Original dictionary
original_dict = {
    "Arfan": ["Computer Science", "Mathematics", "Statistics"],
    "Adnan": ["Computer Science", "Data Structures", "UML"],
    "Aadil": ["Mathematics", "Statistics", "Data Structures"],
}

# Inverted dictionary
print("Original Dictionary:")
for student, courses in original_dict.items():  # Iterate over the key-value pairs
    print(f"Student: {student}")                # Print the student
    print("Courses Enrolled:")
    for course in courses:                      # Print the list of courses
        print(f"- {course}")                    # Print each course
    print()                                     # Print an empty line

inverted_dict = invert_dictionary(original_dict)    # Call the invert_dictionary function
print("\nInverted Dictionary:")                     # Print the inverted dictionary
print_courses_and_students(inverted_dict)           # Call the print_courses_and_students function