### VALORES None
# none es para definir la ausencia de algun valor
response = None

# none es como undefined en js
print(response)

### VALORES FALSOS 

# indicadores de false son 8 en python
"""
  False
  None
  0
  0.0
  '' ó ""
  []
  ()
  {}
"""

print(response == False)
print(not response)

### CONDICIONES
if True or 'todo bien':
  print('verdadero')
elif True:
  pass
else:
  pass

### TERNARIO 

calificacion = 10
color = None

color = 'verde' if calificacion >= 7 else 'rojo'

color = ('verde', 'amarillo')[ calificacion >= 7]

print(color)

### ASIGNAR VALORES MEDIANTE OPERADORES
variable = 'luis' or 'pedro'
print(variable)

listado = [1]
nombres = 'luis'

variable = listado or nombres
print(variable)

### while
count = 0
while count <= 10:
  print(count)
  count += 1
else:
  print('fin del loop')

### FUNCION RANGE Y FUNCION ENUMERATE
secuence = range(1, 5, 2)
for i in secuence:
  print(i)

numeros = [2,2,3,4,5]

for indice, numero in enumerate(numeros, 1):
  print(indice, numero)

### BREAK and CONTINUE
frase = 'curso profesional de python'
for letra in frase:
  if letra == 'o':
    continue
  print(letra)