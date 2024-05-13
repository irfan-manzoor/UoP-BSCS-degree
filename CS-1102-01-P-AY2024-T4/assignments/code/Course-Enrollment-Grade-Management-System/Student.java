import java.util.ArrayList;
import java.util.HashMap;

public class Student {
    private String name;
    private int id;
    private HashMap<Course, Integer> grades;
    private ArrayList<Course> enrolledCourses;

    public Student(String name, int id) {
        this.name = name;
        this.id = id;
        this.grades = new HashMap<>();
        this.enrolledCourses = new ArrayList<>();
    }

    // Getter and setter methods
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

    // Method to enroll student in a course
    public void enrollCourse(Course course) {
        enrolledCourses.add(course);
        course.enrollStudent();
    }

    // Method to assign grade to a student for a course
    public void assignGrade(Course course, int grade) {
        grades.put(course, grade);
    }

    // Method to get grade for a course
    public int getGrade(Course course) {
        return grades.getOrDefault(course, -1);
    }

    // Method to get enrolled courses
    public ArrayList<Course> getEnrolledCourses() {
        return enrolledCourses;
    }
}
