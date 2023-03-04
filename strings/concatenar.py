nombre = 'luis jesus'
paterno = 'villegas'
materno = 'castillo'

saludo = 'Hola {nombre} {materno} {paterno} bienvenido'

print(f'bienvenido {nombre} {paterno} {materno}')
print('bienvenido {} {} {}'.format(nombre, paterno, materno))
print(saludo.format(nombre=nombre, paterno=paterno, materno=materno))

nombre_completo = f'mi nombre es {nombre} {paterno} {materno}'
print(nombre_completo)

# imprecion
print(nombre, materno, paterno, sep=' ')