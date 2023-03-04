lista = ['python', 'js', 'ts', 'docker', 'java']
frameworks = ['angular', 'nextjs', 'nestjs', 'flask']

lista.append('golang')
lista.append('c#')

print(len(lista))

lista.insert(len(lista), 'php' )
print(lista)
print(len(lista))

lista.extend(frameworks)
print(lista)
print(len(lista))

lista.remove('c#')
print(len(lista))

del lista[0]
print(lista)

lista.clear()
print(lista)
