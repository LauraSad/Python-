to_do =["Dirigirnos al hotel",
        "Ir a almorzar",
        "Visitar un museo",
        "Volver al hotel"]
print(to_do)
numbers=[1,2,3,4,"cinco"]
print(numbers)
print(type(numbers))
mix = ["string", 1, 2.5, True, [3, 4]]
print(mix)
print("Primer elemento:",mix[0])
print("Ultimo elemento:",mix[-1])

#Slicing
print(mix[:3])
print(mix[2:])

#Metodos

print(mix)
mix.append(False) #Agrega el elemento al final de la lista
print(mix)
mix.append(["a","b"])
print(mix)
mix.insert(1,["a","b"]) # Agrega el elemento en la posicion elegida
print(mix)
print(mix.index(["a","b"])) #Devuelve la primera aparicion de el elemento
numbers=[1,2,3,4,100.01,99,45,5]
print(numbers)
print("Mayor:",max(numbers))
print("Menor:",min(numbers))

del numbers[-1]
print(numbers)
del numbers [:2]
print(numbers)
del numbers
print(numbers)