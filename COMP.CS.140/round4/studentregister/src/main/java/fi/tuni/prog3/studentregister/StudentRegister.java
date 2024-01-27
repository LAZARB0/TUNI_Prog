package fi.tuni.prog3.studentregister;
import java.util.ArrayList;
import java.util.Collections;
import java.util.Comparator;
import java.util.List;

public class StudentRegister {

    private ArrayList<Student> students;
    private ArrayList<Course> courses;
    private ArrayList<Attainment> attainments;

    public StudentRegister() {
        students = new ArrayList<>();
        courses = new ArrayList<>();
        attainments = new ArrayList<>();
    }

    public ArrayList<Student> getStudents() {
        Collections.sort(students, new Comparator<Student>() {
            @Override
            public int compare(Student s1, Student s2) {
                return s1.getName().compareTo(s2.getName());
            }
        });
        return students;
    }

    public ArrayList<Course> getCourses() {
        Collections.sort(courses, new Comparator<Course>() {
            @Override
            public int compare(Course c1, Course c2) {
                return c1.getName().compareTo(c2.getName());
            }
        });
        return courses;
    }

    public void addStudent(Student student) {
        students.add(student);
    }

    public void addCourse(Course course) {
        courses.add(course);
    }

    public void addAttainment(Attainment attainment) {
        attainments.add(attainment);
    }

    public void printStudentAttainments(String studentNumber, String order) {
        boolean studentExists = false;
        String studentName = "";
        for (Student student : students) {
            if (student.getStudentNumber().equals(studentNumber)) {
                studentExists = true;
                studentName = student.getName();
                break;
            }
        }
    
        if (!studentExists) {
            System.out.println("Unknown student number: " + studentNumber);
            return;
        }
    
        System.out.println(studentName + " (" + studentNumber + "):");
    
        ArrayList<Attainment> studentAttainments = new ArrayList<>();
        for (Attainment attainment : attainments) {
            if (attainment.getStudentNumber().equals(studentNumber)) {
                studentAttainments.add(attainment);
            }
        }
    
        if (order.equals("by name")) {
            Collections.sort(studentAttainments, new Comparator<Attainment>() {
                @Override
                public int compare(Attainment a1, Attainment a2) {
                    String courseName1 = null;
                    String courseName2 = null;
    
                    for (Course course : courses) {
                        if (course.getCode().equals(a1.getCourseCode())) {
                            courseName1 = course.getName();
                        } else if (course.getCode().equals(a2.getCourseCode())) {
                            courseName2 = course.getName();
                        }
                    }
    
                    // Ensure both course names are not null before comparing
                    if (courseName1 != null && courseName2 != null) {
                        return courseName1.compareTo(courseName2);
                    } else {
                        // Handle the case where course names are not found
                        return 0;
                    }
                }
            });
        } else if (order.equals("by code")) {
            Collections.sort(studentAttainments, new Comparator<Attainment>() {
                @Override
                public int compare(Attainment a1, Attainment a2) {
                    return a1.getCourseCode().compareTo(a2.getCourseCode());
                }
            });
        }
    
        for (Attainment attainment : studentAttainments) {
            for (Course course : courses) {
                if (course.getCode().equals(attainment.getCourseCode())) {
                    String courseName = course.getName();
                    System.out.println("  " + attainment.getCourseCode() + " " + courseName + ": " + attainment.getGrade());
                    break;  // Once the matching course is found, break the loop
                }
            }
        }
    }
    
    public void printStudentAttainments(String studentNumber) {
        printStudentAttainments(studentNumber, "default");
    }
}