### GENERADORES
# yield

def pares():# Generador -> lazy iterator
  for numero in range(0, 100, 2):
    yield numero

for par in pares():
  print(par)