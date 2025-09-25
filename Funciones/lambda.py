add = lambda a,b: a+b
print(add(10,4))

multiply = lambda a,b: a*b
print(multiply(10,4))

#Cuadrados de cada numero

numbers = range(11)
square_numers = list(map(lambda x: x**2,numbers))
print("Cuadrados:", square_numers)

#pares
even_numbers = list(map(lambda x: x%2==0,numbers)) # me dice cuales son pares y cuales no con booleanos
print(even_numbers)

even_numbers2 = list(filter(lambda x: x%2==0,numbers)) # filter retorna los valores con valor true
print(even_numbers2)

