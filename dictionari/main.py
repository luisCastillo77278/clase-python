persona = {}
persona_secundaria = dict()

persona['nombre'] = 'luis'
persona['edad'] = 25
persona['ocupacion'] = 'desarollador'

exist_residencia = persona.get('residencia', 'no hay residencia')

print(persona)
print(exist_residencia)

nombre, edad, *_ = persona
print(persona[nombre])
print(persona[edad])

"""
for key, value in persona.items():
  print(key, value)
"""

personas = [
  {
    'nombre': 'luis',
    'edad': 24
  },
  {
    'nombre': 'adriana',
    'edad': 23
  }
]

print('\n')
for persona in personas:
  nombre, edad = tuple(persona.values())
  print(nombre, edad)

# eliminar elementos

