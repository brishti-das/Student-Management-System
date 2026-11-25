class Student:
    def __init__(self, name, student_id,email,age,department):
        self.name = name
        self.student_id = student_id
        self.__email = email
        self.age = age
        self.department = department

    def get_email(self):
        return self.__email

    def display_info(self):
        print("Name: ", self.name)
        print("Student ID: ", self.student_id)
        print("Email: ", self.get_email())
        print("Age: ", self.age)
        print("Department: ", self.department)

    def calculate_result(self, *marks):
        if len(marks) == 0:
            return "No marks provide"

        total = sum(marks)
        avg = total/len(marks)

        return round(avg,2)

    def get_student_type(self):
        return "General Student"

class UndergraduateStudent(Student):
    def __init__(self, name, student_id,email,age,department,semester):
        super().__init__(name,student_id,email,age,department)
        self.semester = semester

        def get_student_type(self):
            return "Undergraduate Student."

class  GraduateStudent(Student):
    def __init__(self, name, student_id,email,age,department,research_topic):
        super().__init__(name,student_id,email,age,department)
        self.research_topic = research_topic

        def get_student_type(self):
            return "Graduate Student"


student1 = Student(
    "Tuki",
    "101",
    "tuki@gmail.com",
    17,
    "EEE"
)
student1.display_info()
print("Student Type: ", student1.get_student_type())
print("Result: ", student1.calculate_result(94, 84,71,90),"\n")

student2 = UndergraduateStudent(
    "Tuktuki",
    "102",
    "tuktuki@gmail.com",
    21,
    "CSE",
    6
)        

student2.display_info()
print("Semester: ",student2.semester)
print("Student Type: ",student2.get_student_type())
print("Undergraduate Result:", student2.calculate_result(82,86,91),"\n")

student3 = GraduateStudent(
    "Tuku",
    "103",
    "tuku@gmail.com",
    25,
    "DS",
    "Machine Learning for Healthcare Prediction"
)
student3.display_info()
print("Student Type: ", student3.get_student_type())
print("Research Topic: ", student3.research_topic)
print("Undergraduate Result:", student3.calculate_result(81,88,90,98))
