numbers = {1:"uno",2:"dos",3:"tres"}
print(numbers)
print(numbers[2]) # Para ver la informacion de la llave

information= {"nombre":"Laura",
              "Apellido":"Moreno",
              "Altura": 1.60,
              "Edad": 23
              }
print(information)
del information["Edad"]
print(information)

claves =information.keys() # Obtener las claves
print(claves)
print(type(claves))
values= information.values() # Obtener los valores
print(values)
pairs = information.items() 
# Obtener los pares clave-valor
print(pairs)

contacts = {"Laura":{"Apellido":"Moreno",
              "Altura": 1.60,
              "Edad": 23},
              "Marlon":{"Apellido":"Jimenez",
              "Altura": 1.70,
              "Edad": 19}
              }

print(contacts["Marlon"])