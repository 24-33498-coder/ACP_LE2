class Student:
    id_name = ()
    email = ()
    grades = {}
    courses = ()

    def __init__(self, student_id, student_name, email, grades=None, courses=None):
        self.student_id = student_id
        self.student_name = student_name
        self.email = email
        self.grades = grades
        self.courses = courses

class StudentsRecords:
    Studentlist = ()
    def __init__(self):
        pass 
