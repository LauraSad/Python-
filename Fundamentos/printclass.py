x = 1
y = 1.5
z = 1.2E6
w = 1.2E-6
print(type(x))
print(type(y))
print(z)
print(w)
print(x + y)

print("Diferentes formas de imprimir")
print("Diferentes","formas","de","imprimir") #la coma añade automaticamente un espacio entre los argumentos
print('Diferentes' + 'formas' + 'de' + "imprimir") #al concatenar cadenas con el operador + los elementos se unen sin un espacio adicional
print("Asi" + " " + "se pone un espacio")


#SEP permite especificar como separ los elementos al imprimir
print("Diferentes","formas","de","imprimir", sep= " x ")

#END cambia lo que se imprime al final de la llamada a print
print("Nunca", end=" ")
print("Pares de aprender", end=" ")
print("HOla")

frase = "Nunca pares de aprender"
author = "Platzi"
print("Frase:", frase, "Autor:", author)

#f-strings:
#Hace que el codigo sea mas legible y facil de escribir
frase = "Nunca pares de aprender"
author = "Platzi"
print(f"Frase: {frase}, Autor: {author}")

#format es un metodo usado para insertar valores en cadenas de text. Usando {} como marcadores de posicion 
frase = "Nunca pares de aprender"
author = "Platzi"
print("Frase: {}, Autor: {} ".format(frase,author))

#impresion con formato especifico 2f indica que el numero debe mostrarse con dos decimales lo redondea despues de .5
valor = 3.14559
print("Valor: {: .2f}".format(valor))

# SALTOS DE LINEA Y CARACTERES ESPECIALES
print("Hola\nmundo") #salto de linea se indican con la secuencia de escape \n
print('Hola soy \'Laura\'')
#print('HOla soy 'Laura' ') da error syntax
print("La ruta de archivo es: C:\\Users\\Usuario\\Desktop\\archivo.txt") # si no se pone doble \ da error

