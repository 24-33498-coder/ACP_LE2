class Student:
   
    def __init__(self, student_id, student_name, email, grades=None, courses=None):
        self.name_id = (student_id, student_name)
        self.email = email
        self.grades = grades if grades is not None else {}
        self.courses = courses if courses is not None else set ()

    def __str__(self):
        return (f"STudent ID: {self.name_id[0]}, "
                f"Student Name: {self.name_id[1]}, Email: {self.email}, "
                f"Student Grades: {self.grades if self.grades is not None else "None"}, "
                f"Courses: {self.courses if self.courses is not None else "None"}")

    def calculate_gpa(self):

        if not self.grades:
            return None
        total = 0
        count = 0

        for score in self.grades.values():
            if isinstance(score, str):
                grade = score.upper()
                gpa = {'Z': 4.0, 'Y': 3.0, 'X': 2.0, 'W': 1.0, 'V': 0.0}.get(grade, 0.0)
            else:

                if score >= 90:
                    gpa = 4.0
                elif score >= 80:
                    gpa = 3.0
                elif score >= 70:
                    gpa = 2.0
                elif score >= 60:
                    gpa = 1.0
                else:
                    gpa = 0.0
            total += gpa
            count += 1
        return round(total / count, 2) if count else None

class StudentRecords:
    def __init__(self):
        self.students = []

    def add_student(self, student_id, student_name, email, grades=None, courses=None):

        newstudent = Student(student_id, student_name, email, grades, courses)
        self.student.append(newstudent)

        return "Student added successfully"

    def update_student(self, student_id, email=None, grades=None, courses=None):
        for student in self.students:
            if student.name_id[0] == student_id:
                if email:
                    student.email = email
                if grades:
                    student.grades = grades
                if courses:
                    student.courses = courses
                return "Student updated successfully"
            return "Student not found"
    def delete_student(self, student_id):
        for i, student in enumerate(self.students):
            if student.name_id[0] == student_id:
                del self.students[i]
                return "Student deleted successfully"
        return "Student not found"

    def enroll_courses(self, student_id, course):
        for student in self.students:
            if student.name_id[0] == student_id:
                student.courses.add(course)
                return "Courses added successfully"
            return "Student not found
    
