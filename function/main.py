### RETURN 
# Los return en python pueden ser multiples
# nota: solo retornar un maximo de 3 valores
# cuando son multiples valores python los agrupa en tuplas
def suma (n1, n2):
  return n1 + n2, 'la funcion retorna 2 valores', True

sumas, *resto = suma(10, 10)
print(sumas)
print(resto)

sumar, *_ = suma(10, 10)
print(sumar)

### PARAMETROS OPCIONALES
def area_circulo(radio, pi = 3.1416):
  return pi * (radio ** 2)

resultado = area_circulo(radio=10, pi=3.14)
print(resultado)

### ARGS
# por convencion los parametros con asterisco deben llamarse args
def multiples_args(*args): # tuple
  print(args)

multiples_args(1,2,3,5)
# Nota dos saltos entre cada funcion
def combinacion(p1,p2,p3, *args, p4=500):
  print(p1)
  print(p2)
  print(p3)
  print(args)
  print(p4)

combinacion(1,2,3,4,5,6,p4=100)

### KWARGS
def usuarios(**kwargs): # dict
  print(kwargs)

usuarios(eduardo=[10,10,10], fernando=[9,10,8])
usuarios(nombre='luis', edad=24)

### scope
animal = 'leon'

def imprimir_animal():
  animal = 'cebra'
  # global animal
  # animal = 'tigre'
  print(animal)

imprimir_animal()
print(animal)

### FUNCIONES ANIDADAS
def operacion(cantidad, valance, tipo='deposito'):

  def deposito(cantidad, valance):
    return cantidad + valance


  def retiro(cantidad, valance):
    if cantidad <= valance:
      return valance - cantidad
    else:
      return None


  if tipo == 'deposito':
    return deposito(cantidad, valance)
  else:
    return retiro(cantidad, valance)

print(operacion(10, 20))

### FUNCIONES DE PRIMER ORDER
### LAS FUNCIONES SON CIUDADANOS DE PRIMER ORDEN COMO EN JS
def centigrados_a_farhenheit(grados):
  return grados * 1.8 + 32

my_function = centigrados_a_farhenheit

print(type(my_function))
print(my_function(10))

### FUNCIONES LAMBDA Ó ANONIMA
funcion_grados = lambda grados : grados * 1.8 + 32
# lambda params: body function
### return queda de forma implicita como en arrow function

print(funcion_grados(10))

result = map(lambda n: n*2, (1,2,3,4,5))
print(list(result))

filtro = filter(lambda n: n > 10, (1,2,20,30,0,100))
print(tuple(filtro))

### CALLBACK
promedio = lambda *args : sum(args) / len(args)

aprobatorio = lambda calificacion : calificacion >= 7

print(promedio(10,10,9,8,7))

def mostrar_mensage(cb_promedio, cb_aprobatorio, *args):
  promedio = cb_promedio(*args)
  is_aprobatorio = cb_aprobatorio(promedio)

  if (is_aprobatorio):
    print(f'aprobo: promedio {promedio}')
  else:
    print(f'no aprobo: promedio {promedio}')


mostrar_mensage(promedio, aprobatorio, 10,10,9,8,7)

#### VARIABLES NO LOCALES CLOUSURE
e = 'e'
def funcion_principal():
  a = 'a'
  b = 'b'


  def function_anidada():
    c = 'c' # variables locales
    
    global e
    e = 'cambie'
    
    nonlocal b # esto cuando la variable local esta en un nivel superior 
    b = 'cambio de valor'
    print(a)
    print(b)
    print(e)

  function_anidada()
  print(b)

funcion_principal()
print(e)

### RETORNAR FUNCIONES

def saludar ():

  def mostrar_mensaje():
    print('hola mundo con python funcion return')

  return mostrar_mensaje


# saludar()() esta es una opcion
mensaje = saludar()
mensaje()

### CLOUSURES

def saludar(username):

  mensaje = f'hola {username}'

  def mostrar_message():
    print(f'{mensaje} desde clousure')

  return mostrar_message


respuesta = saludar('luis jesus')
respuesta()

### DECORADORES
"""
  a -> la funcion principal (decorador)
  b -> la funcion del decorador
  c -> la funcion decorada

  a(b) -> c
"""

def funcion_a(funcion_b):

  def funcion_c():
    numero = 1
    print('extendiendo')
    
    funcion_b(numero)
    
    print('extendiendo mas')

  return funcion_c

@funcion_a
def saludar(numero):
  print(f'hola nos encontramos en una funcion {numero}')

saludar()