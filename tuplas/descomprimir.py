# * asteristco antes de una variable es una lista
# _ omitir valores
numeros = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
#uno, dos, tres, cuatro, *resto_numeros = numeros
uno, dos, tres, cuatro, *_, nueve, diez = numeros


print(uno)
print(dos)
print(tres)
print(cuatro)
print(nueve)
print(diez)
