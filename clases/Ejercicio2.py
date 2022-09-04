class Saludos:
    def __init__(self, nombre):
        self.nombre = nombre

    def saludo(self, otrapersona):
        return f'Hola amigo {otrapersona.nombre}, soy {self.nombre}'


if __name__ == '__main__':
    Pedro = Saludos('Pedro')
    Juan = Saludos('Juan')

    print(Pedro.saludo(Juan))
    print(Juan.saludo(Pedro))
