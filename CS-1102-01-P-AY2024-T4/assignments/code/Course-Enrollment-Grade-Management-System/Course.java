public class Course {
    private String courseCode;
    private String name;
    private int maxCapacity;
    private int enrolledStudents;

    public Course(String courseCode, String name, int maxCapacity) {
        this.courseCode = courseCode;
        this.name = name;
        this.maxCapacity = maxCapacity;
        this.enrolledStudents = 0;
    }

    // Getter methods
    public String getCourseCode() {
        return courseCode;
    }

    public String getName() {
        return name;
    }

    public int getMaxCapacity() {
        return maxCapacity;
    }

    public int getEnrolledStudents() {
        return enrolledStudents;
    }

    // Method to enroll a student in the course
    public void enrollStudent() {
        enrolledStudents++;
    }
}
