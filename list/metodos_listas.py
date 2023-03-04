lista = [8, 90, 1, 5, 44, 132, 600, 3, 4]

lista.sort()
# ordenamiento desendente de mayor a menor
lista.sort(reverse=True)


print(lista)
print(min(lista))
print(max(lista))
print(5 in lista)
print(10 not in lista)

# index method retorna la primera coincidencia
index = lista.index(5)
print(index)
