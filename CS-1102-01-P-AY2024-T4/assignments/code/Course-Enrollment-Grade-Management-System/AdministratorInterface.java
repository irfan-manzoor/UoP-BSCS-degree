import java.util.Scanner;

public class AdministratorInterface {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        boolean exit = false;

        while (!exit) {
            System.out.println("1. Add new course");
            System.out.println("2. Enroll student");
            System.out.println("3. Assign grade");
            System.out.println("4. Calculate overall course grade");
            System.out.println("5. Exit");
            System.out.print("Enter your choice: ");
            int choice = scanner.nextInt();
            scanner.nextLine(); // Consume newline character

            switch (choice) {
                case 1:
                    addNewCourse(scanner);
                    break;
                case 2:
                    enrollStudent(scanner);
                    break;
                case 3:
                    assignGrade(scanner);
                    break;
                case 4:
                    calculateOverallGrade(scanner);
                    break;
                case 5:
                    exit = true;
                    break;
                default:
                    System.out.println("Invalid choice. Please try again.");
            }
        }
        scanner.close();
    }

    private static void addNewCourse(Scanner scanner) {
        System.out.print("Enter course code: ");
        String courseCode = scanner.nextLine();
        System.out.print("Enter course name: ");
        String courseName = scanner.nextLine();
        System.out.print("Enter maximum capacity: ");
        int maxCapacity = scanner.nextInt();
        CourseManagement.addCourse(courseCode, courseName, maxCapacity);
        System.out.println("Course added successfully.");
    }

    private static void enrollStudent(Scanner scanner) {
        System.out.print("Enter student name: ");
        String studentName = scanner.nextLine();
        System.out.print("Enter student ID: ");
        int studentId = scanner.nextInt();
        Student student = new Student(studentName, studentId);
        System.out.print("Enter course code to enroll in: ");
        String code = scanner.next();
        Course course = findCourseByCode(code);
        if (course != null) {
            CourseManagement.enrollStudent(student, course);
            System.out.println("Student enrolled successfully.");
        } else {
            System.out.println("Course not found.");
        }
    }

    private static void assignGrade(Scanner scanner) {
        System.out.print("Enter student ID: ");
        int id = scanner.nextInt();
        Student student = findStudentById(id);
        if (student != null) {
            System.out.print("Enter course code: ");
            String code = scanner.next();
            Course course = findCourseByCode(code);
            if (course != null) {
                System.out.print("Enter grade: ");
                int grade = scanner.nextInt();
                CourseManagement.assignGrade(student, course, grade);
                System.out.println("Grade assigned successfully.");
            } else {
                System.out.println("Course not found.");
            }
        } else {
            System.out.println("Student not found.");
        }
    }

    private static void calculateOverallGrade(Scanner scanner) {
        System.out.print("Enter student ID: ");
        int id = scanner.nextInt();
        Student student = findStudentById(id);
        if (student != null) {
            double overallGrade = CourseManagement.calculateOverallGrade(student);
            System.out.println("Overall course grade for student " + student.getName() + " (ID: " + student.getId() + "): " + overallGrade);
        } else {
            System.out.println("Student not found.");
        }
    }

    private static Course findCourseByCode(String code) {
        for (Course course : CourseManagement.getCourses()) {
            if (course.getCourseCode().equals(code)) {
                return course;
            }
        }
        return null;
    }

    private static Student findStudentById(int id) {
        for (Student student : CourseManagement.getStudents()) {
            if (student.getId() == id) {
                return student;
            }
        }
        return null;
    }
}
