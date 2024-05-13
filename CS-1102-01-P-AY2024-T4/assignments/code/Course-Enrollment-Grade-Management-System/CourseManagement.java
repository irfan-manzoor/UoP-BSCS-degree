import java.util.ArrayList;

public class CourseManagement {
    private static ArrayList<Course> courses = new ArrayList<>();
    private static ArrayList<Student> students = new ArrayList<>();

    // Static method to add new course
    public static void addCourse(String courseCode, String name, int maxCapacity) {
        Course course = new Course(courseCode, name, maxCapacity);
        courses.add(course);
    }

    // Static method to enroll a student in a course
    public static void enrollStudent(Student student, Course course) {
        if (course.getEnrolledStudents() < course.getMaxCapacity()) {
            student.enrollCourse(course);
            students.add(student);
        } else {
            System.out.println("Course has reached maximum capacity.");
        }
    }

    // Static method to assign grade to a student for a course
    public static void assignGrade(Student student, Course course, int grade) {
        student.assignGrade(course, grade);
    }

    // Static method to calculate overall course grade for a student
    public static double calculateOverallGrade(Student student) {
        double totalGrade = 0.0;
        int numCourses = 0;

        for (Course course : student.getEnrolledCourses()) {
            int grade = student.getGrade(course);
            if (grade != -1) {
                totalGrade += grade;
                numCourses++;
            }
        }

        if (numCourses == 0) {
            return 0.0;
        }

        return totalGrade / numCourses;
    }

    // Getter method for courses
    public static ArrayList<Course> getCourses() {
        return courses;
    }

    // Getter method for students
    public static ArrayList<Student> getStudents() {
        return students;
    }
}
