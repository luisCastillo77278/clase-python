def function_a(function_b):

  def function_c(*args, **kwargs):
    print(args)
    print(kwargs)
    return function_b(*args, **kwargs)

  return function_c


@function_a
def suma(numero1, numero2):
  return numero1 + numero2


rerultado = suma(10, 20)
print(rerultado)