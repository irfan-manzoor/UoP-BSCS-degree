import java.util.Scanner;

// Student class to represent individual student objects
class Student {
    private String name;
    private int id;
    private int age;
    private String grade;

    // Constructor to initialize student properties
    public Student(String name, int id, int age, String grade) {
        this.name = name;
        this.id = id;
        this.age = age;
        this.grade = grade;
    }

    // Getters and setters for accessing and modifying student properties
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public int getId() {
        return id;
    }

    public void setId(int id) {
        this.id = id;
    }

    public int getAge() {
        return age;
    }

    public void setAge(int age) {
        this.age = age;
    }

    public String getGrade() {
        return grade;
    }

    public void setGrade(String grade) {
        this.grade = grade;
    }
}

// StudentManagement class to manage student-related operations
class StudentManagement {
    private static int totalStudents = 0;
    private static Student[] students = new Student[100]; // Assuming max 100 students

    // Method to add a new student to the system
    public static void addStudent(String name, int id, int age, String grade) {
        Student student = new Student(name, id, age, grade);
        students[totalStudents++] = student; // Add student to the array and increment totalStudents
        System.out.println("Student added successfully!");
    }

    // Method to update information of an existing student
    public static void updateStudent(int id, String newName, int newAge, String newGrade) {
        for (int i = 0; i < totalStudents; i++) {
            if (students[i].getId() == id) {
                // Update student information if the ID matches
                students[i].setName(newName);
                students[i].setAge(newAge);
                students[i].setGrade(newGrade);
                System.out.println("Student information updated successfully!");
                return;
            }
        }
        // If student ID not found
        System.out.println("Student ID not found!");
    }

    // Method to view details of a specific student
    public static void viewStudentDetails(int id) {
        for (int i = 0; i < totalStudents; i++) {
            if (students[i].getId() == id) {
                // Display student details if ID matches
                System.out.println("Name: " + students[i].getName());
                System.out.println("ID: " + students[i].getId());
                System.out.println("Age: " + students[i].getAge());
                System.out.println("Grade: " + students[i].getGrade());
                return;
            }
        }
        // If student ID not found
        System.out.println("Student ID not found!");
    }
}

// Main class to handle user interactions and execute the program
public class StudentRecordManagementSystem {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int choice;

        // Main menu loop to keep the program running until the user chooses to exit
        do {
            // Display menu options
            System.out.println("\nStudent Record Management System");
            System.out.println("1. Add New Student");
            System.out.println("2. Update Student Information");
            System.out.println("3. View Student Details");
            System.out.println("4. Exit");
            System.out.print("Enter your choice: ");
            choice = scanner.nextInt();

            switch (choice) {
                case 1:
                    // Adding a new student
                    System.out.print("Enter student name: ");
                    String name = scanner.next();
                    System.out.print("Enter student ID: ");
                    int id = scanner.nextInt();
                    System.out.print("Enter student age: ");
                    int age = scanner.nextInt();
                    System.out.print("Enter student grade: ");
                    String grade = scanner.next();
                    StudentManagement.addStudent(name, id, age, grade);
                    break;
                case 2:
                    // Updating student information
                    System.out.print("Enter student ID to update: ");
                    int updateId = scanner.nextInt();
                    System.out.print("Enter new name: ");
                    String newName = scanner.next();
                    System.out.print("Enter new age: ");
                    int newAge = scanner.nextInt();
                    System.out.print("Enter new grade: ");
                    String newGrade = scanner.next();
                    StudentManagement.updateStudent(updateId, newName, newAge, newGrade);
                    break;
                case 3:
                    // Viewing student details
                    System.out.print("Enter student ID to view details: ");
                    int viewId = scanner.nextInt();
                    StudentManagement.viewStudentDetails(viewId);
                    break;
                case 4:
                    // Exiting the program
                    System.out.println("Exiting...");
                    break;
                default:
                    // Handling invalid choice
                    System.out.println("Invalid choice!");
            }
        } while (choice != 4); // Repeat until the user chooses to exit
        scanner.close(); // Close the scanner to avoid resource leaks
    }
}