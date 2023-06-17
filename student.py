class Student():
    def __init__(self,name,student_id,age,grades) :
        self.name=name
        self.student_id=student_id
        self.age=age
        self.grades=[]
        self.grades.append[grades]
    def display(self):
        print("name: ",self.name)
        print("student_id: ", self.student_id)
        print("age: ",self.age)
        print("grades: ",self.grades )
class StudentManagementSystem():
    def __init__(self) :
        self.inbox=[]
    def add_student(self,student):
        self.inbox.append[student]
    def search(self,id):
        self.id=id
        for id in self.inbox:
            if id ==  self.id:
                self.display()
                print("-------------------------------")
    def caculate_average(self):
        average=0
        for i in self.inbox:
            average=sum(self.grades)/len(self.grades)
            average+=average
        average=average/len(self.inbox)
        return average
        



        