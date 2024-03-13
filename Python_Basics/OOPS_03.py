class Student:
    def __init__(self, name, rollno, marks):
        self.name = name
        self.rollno = rollno
        self.marks = marks
    def talk(self):
        print("Hello I am: ", self.name)
        print("My roll number: ", self.rollno)
        print("My marks: ", self.marks) 

s1 = Student("Sunny", 101, 90)
s2 = Student("Bunny", 102, 95)
s1.talk()
s2.talk()