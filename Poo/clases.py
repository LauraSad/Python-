class Person:
    def __init__(self, name, age):
        pass
        self.name = name
        self.age = age

    def greet(self):  #Metodo
        print(f"Hola, mi nombre es {self.name} y  y tengo {self.age}")

class Student(Person):
    def __init__(self, name, age,student_id):
        super().__init__(name, age)
        self.student_id = student_id

    def greet(self):
        super().greet()
        print(f"Hello, mi student ID is {self.student_id}")

student1 = Student("Anna",20, "s1234")
student1.greet()