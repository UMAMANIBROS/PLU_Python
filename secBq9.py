# 9. Create a Student class with name and age, then display them
class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def display(self):
        print("Name:", self.name)
        print("Age:", self.age)
s1 = Student("Shankar", 20)
s1.display()