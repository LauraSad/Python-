numbers = [1,2,3,4,5,6]
for i in numbers:
    print("aqui i es igual a:",i)

for i in range(3,10):
    print(i)

fruits = ["manzana", 'pera', 'uva','naranja', 'tomate',]
for fruit in fruits:
    print(fruit)
    if fruit == 'naranja':
        print("Naranja encontrada")

#WHILE (mientras se cumpla la condicion vamos a entrar en la condicion)
x = 0
while x<5:
    if x == 3:
        break ## El codigo termina cuando se cumple la condicion
    print(x)
    x += 1  #Condicion para que se detenga en algun momento



numbers = [1,2,3,4,5,6]
for i in numbers:
    if i == 3:
        continue #Omite cuando se cumple la condicion
    print("aqui i es igual a:",i)


