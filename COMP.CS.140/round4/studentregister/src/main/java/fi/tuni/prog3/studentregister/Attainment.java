package fi.tuni.prog3.studentregister;

public class Attainment {
    private String studentNumber;
    private String courseCode;
    private int grade;

    public Attainment(String courseCode, String studentNumber, int grade) {
        this.studentNumber = studentNumber;
        this.courseCode = courseCode;
        this.grade = grade;
    }

    public String getStudentNumber() {
        return studentNumber;
    }

    public String getCourseCode() {
        return courseCode;
    }

    public int getGrade() {
        return grade;
    }
}
