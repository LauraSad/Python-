##Conceptos basicos de POO
#Atributos Son variables que pertenecen a una clase o a un objeto.
#Metodos Son funciones que pertenecen a una clase o a un objeto. Definen el comportamiento de los objetos.
#Clase Es una plantilla o un molde que define las propiedades y comportamientos comunes de un conjunto de objetos.

#creamos una instancia de la clase Persona 
#

#Herencia al usar herencia vimos el método init() que es le constructor, el mismo es llamado automáticamente cuando se crea una nueva instancia de una clase y se utiliza para inicializar los atributos del objeto.

#Constructor
class Animal:
    def __init__(self, especie): 
        self.especie = especie
#CREAR UNA INSTANCIA DE LA CLASE ANIMAL
animal1 = Animal("Perro") #INIT INICIA EL ATRIBUTO ESPECIE
print(animal1.especie) #Output: Perro

#SUPER()
#La función super() se utiliza para llamar a un método de la clase padre desde una clase hija. Esto es útil cuando se quiere extender o modificar el comportamiento de un método heredado sin sobrescribirlo completamente.

class Persona:
    #Atributos
    def __init__(self, nombre, edad):
        self.nombre = nombre  #atributo de instancia
        self.edad = edad #atributo de instancia

    #Metodos
    def saludar(self):
        print("Hola, Im a person")
    
class Student(Persona):
    def __init__(self, nombre, edad, student_id):
        super().__init__(nombre, edad) #Llama al constructor de la clase padre (Persona) para inicializar los atributos heredados.
        self.student_id = student_id #Atributo especifico de la clase Student   
    def saludar(self):
        super().saludar() #Llama al método saludar() de la clase padre (Persona).
        print(f"Hi, I'm {self.nombre}, {self.edad} years old, my student ID {self.student_id}")

student = Student("Laura", 23, 1002458538)
student.saludar() #Output: Hi, I'm Laura, 23 years old, my student ID 1002458538


#Jerarquia de clases
class LivingBeing:
    def __init__(self, name):
        self.name = name

class Person(LivingBeing):
    def __init__(self, name, age):
        super().__init__(name)
        self.age = age

class Student(Person):
    def __init__(self, name, age, student_id):
        super().__init__(name, age)
        self.student_id = student_id

    def introduce(self):
        print(f"Hi, I'm {self.name}, {self.age} years old, and my student ID is {self.student_id}")

# Crear instancia de Student
student = Student("Carlos", 21, "S54321")
student.introduce()  # Output: Hi, I'm Carlos, 21 years old, and my student ID is S54321

#LivingBeing -> Person -> Student

#Metodos comunes en Python
#__init__(self) Constructor de la clase.    
#__str__(self) Representación en cadena del objeto.
#__repr__(self) Representación oficial del objeto, útil para depuración.
#__eq__(self, other) Compara si dos objetos son iguales.

#ejemplo de __str__ y _repr__
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return f"Point({self.x}, {self.y})"

    def __repr__(self):
        return f"Point(x={self.x}, y={self.y})"
    def __eq__(self, other):
        if isinstance(other, Point):
            return self.x == other.x and self.y == other.y
        return False    
# Crear instancia de Point
point1 = Point(2, 3)
point2 = Point(2, 3)
print(point1)          # Output: Point(2, 3) - Llama a __str__
print(repr(point1))    # Output: Point(x=2, y=3) - Llama a __repr__
print(point1 == point2) # Output: True - Llama a __eq__