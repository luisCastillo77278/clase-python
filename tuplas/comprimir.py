"""
nota: lo aconsejable es trabajar este temas de
comprecion con tuplas 

si hay mas elementos en una tupla, estos son
ignorados
"""

lista = [1,2,3,4,5]

tupla = (10,20,30,40,50)

tupla_3 = (100,200,300,400,500)

tuple_4 = (1000,2000,3000,4000,5000)

resultado = zip(tupla, lista, tupla_3, tuple_4) # return object zip

resultado = tuple(resultado)

print(resultado)
