class Saludos:
    def __init__(self, nombre):
        self.nombre = nombre

    def saludo(self):
        return f'Hola amigo, soy {self.nombre}'


if __name__ == '__main__':
    Pedro = Saludos('Pedro')
    Juan = Saludos('Juan')

    print(Pedro.saludo())
    print(Juan.saludo())
