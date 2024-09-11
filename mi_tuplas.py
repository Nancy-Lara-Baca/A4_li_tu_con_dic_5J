print("Ejemplo de tuplas")
canciones=("intro","canela","la curiosidad")
print(canciones)

y = list(canciones)
print(y)
y[1] = "cambio de papeles"
x = tuple(y)

print(x)
print("Listado de elementos de la tupla canciones ciclo for")
for lara in canciones:
    print(lara)