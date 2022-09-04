# definicion de clases

class Persona:
    def __init__(self, nombre, edad, genero):
        self.nombre = nombre
        self.edad = edad
        self.genero = genero

    def saluda(self, otrapersona):
        return f'Hola {otrapersona.nombre}, me llamo {self.nombre} y soy {self.genero}, y tu eres {otrapersona.genero}'

    def baila(self, otrapersona, tercerapersona):
        return f'Hola soy {self.nombre}, {otrapersona.nombre} quieres ir a bailar con {tercerapersona.nombre}'


if __name__ == '__main__':
    david = Persona('David', 12, 'Masculino')
    erika = Persona('Erika', 16, 'Femenino')
    joshua = Persona('Joshua', 19, 'Masculino')

    print(david.saluda(erika))
    print(erika.saluda(david))
    print(joshua.baila(erika, david))
