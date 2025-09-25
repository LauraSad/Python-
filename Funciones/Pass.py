try:
    divisor = int(input("Ingresa un numero divisor: "))
    resultado = 100 / divisor
except ZeroDivisionError as e:
    print("Error: El divisor no puede ser cero")
    print("Ha ocurrido un error",e)
except ValueError as e:
    print("Error: Debes introducir un numero valido ")
    print("Ha ocurrido un error",e)
numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
transformados = [x * 2 if x % 2 == 0 else x for x in numeros]
print("Números transformados:", transformados)
