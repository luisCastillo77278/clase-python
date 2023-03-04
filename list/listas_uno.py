lista = ['string', 1, 1.43, True] #  lista
lista2 = list(range(0,5))
print(lista)
print(lista2)

# actualizar listas
lista2[1] = 3
print(lista2)

# sublistas
# [start:end]
# lista2[1:] esto es igual nos trae de la posocion asta la ultima
# lista2[:4] obtenemos del primer indice hasta el fila
# lista2[start:end:skip] podemos generar saltos para generar sublistas

sub_lista = lista2[0:3]
sub_lista2 = lista2[1:50] 
sub_lista3 = lista2[:4]
sub_lista4 = lista2[1:5:2]
sub_lista5 = lista2[::2]
sub_lista6 = lista2[::]
sub_lista7 = lista2[::-1]


print(sub_lista)
print(sub_lista2)
print(sub_lista3)
print(sub_lista4)
print(sub_lista5)
print(sub_lista6)
print(sub_lista7)

