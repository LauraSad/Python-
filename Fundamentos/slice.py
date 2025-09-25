a= [1,2,3,4,5]
b=a
print(a)
print(b)
del a[0]
print(a)
print(b)
print(id(a)) # mismo espacio en memoria
print(id(b))

c= a[:] #copiar toda la lista pero diferente posicion
print(id(a[-1]))
print(id(c[-1]))

a.append("frijol")
print(a)
print(b)
print(c)

d= a.copy() #Los elementos tienen la misma posicion en memoria cuando se copian
print(id(a))
print(id(d))

print(id(a[2]))
print(id(d[2]))