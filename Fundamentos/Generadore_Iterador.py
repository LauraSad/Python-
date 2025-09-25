#Ejemplo de iterador


#Crear una lista
my_list = [1,2,3,4]

#Obtener el iterador

my_iter = iter(my_list)

#usar el iterador para obtener los elementos

print(next(my_iter))
print(next(my_iter))
print(next(my_iter))
print(next(my_iter))

#Iterar en cadenas

#creando la cadena 
text = "Hola mundo"

#iterando en la cadena
iter_text = iter(text)

#Iterar en la cadena

for char in iter_text:
    print(char)

#Crear un iterador para los numeros impares

limit = 10

odd_itter = iter(range(1,limit+1,2))

#Usar el iterador
for num in odd_itter:
    print("numeros",num)

#Generador

def my_generator():
    yield 1
    yield 2
    yield 3

for value in my_generator():
    print(value)


#Creando la serie de fibonacci

# 0 1 1 2 3 5 8 13 21 ...

def fibonacci(limit):
    a,b = 0,1
    while a< limit:
        yield a
        a,b = b, a + b
for num in fibonacci(10):
    print(num)