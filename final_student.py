class Student():
    def __init__(self, name, student_id, age):
        self.name = name
        self.student_id = student_id
        self.age = age
        self.grades = []

    def add_grade(self, grade):
        self.grades.append(grade)

    def display(self):
        print("name:", self.name)
        print("student_id:", self.student_id)
        print("age:", self.age)
        print("grades:", self.grades)


class StudentManagementSystem():
    def __init__(self):
        self.students = []

    def add_student(self, student):
        self.students.append(student)

    def search(self, student_id):
        for student in self.students:
            if student.student_id == student_id:
                student.display()
                print("-------------------------------")

    def calculate_average(self):
        total_grades = 0
        num_students = len(self.students)
        for student in self.students:
            total_grades += sum(student.grades)
        if num_students > 0:
            average = total_grades / num_students
        else:
            average = 0
        return average
# 建立學生物件1
student1 = Student("John", "001", 18)
student1.add_grade(85)
student1.add_grade(90)

# 建立學生物件2
student2 = Student("Alice", "002", 20)
student2.add_grade(78)
student2.add_grade(92)
# 建立學生管理系統物件
system = StudentManagementSystem()
# 新增學生到學生管理系統
system.add_student(student1)
system.add_student(student2)
# 查詢學生資訊
system.search("001")
