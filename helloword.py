print('')

# guia de estilo de codificaion PEP-8

# las clases llevan la nomenclatura camelkeys
# los espacios deben ser 4

class User():
    def __init__(self, username, password=''):  #parametros van de esta forma
        self.username = username
        self.password = password

    # metodos igual utilizan snackeys
    def set_password(self, password):
        self.password = password


# las variables deben escribirse con la sintaxis snackeys
condy_user = User('cody')
print(condy_user.username)
#  todos los archivos deben finalizar con un espacio


# para crear entornos virtuales de desarollo
# python -m venv nombreDelEntorno es recomendable que sea env
# para activar el entorno source env/bin/activate
# para desactivar el entorno deactivate
# pip install -r archivo.txt para instalar dependencias desde un archivo
