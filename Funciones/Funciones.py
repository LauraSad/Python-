def greet(name,last_name="No tiene apellido"):
    print("Hola", name,last_name)

greet("Laura","Moreno")
greet("Marlon")
greet(last_name="Moreno",name="Laura")

#calculadora

#suma
def add(a,b):
    return a+b

def subtract(a,b):
    return a-b

def multiply(a,b):
    return a*b

def divide(a,b):
    return a/b

def calculator():
    while True:
        print("Seleccione una operacion")
        print("1. Suma")
        print("2. Resta")
        print("3. Multiplicacion")
        print("4. Division")
        print("5. Salir")

        option = input("Ingrese su opcion (1,2,3,4,5): ")

        if option == "5":
            print("Esta saliendo de la calculadora")
            break
        
        if option in ["1","2","3","4"]:
            num1 = float(input("Ingrese el primer numero: "))
            num2 = float(input("Ingrese el segundo numero: "))

            if option == "1":
                print( "La suma es:", add(num1,num2))
            elif option == "2":
                print( "La resta es:", subtract(num1,num2))
            elif option == "3":
                print( "La multiplicacion es:", multiply(num1,num2))
            elif option == "4":
                print( "La division es:", divide(num1,num2))
        else:
                print("Por favor introduzca una opcion valida")
calculator()

            
