class Frecuencia:
    def __init__(self, texto):
        self.texto = texto

    def generar(self):
        quitar = ",;:.\n!\"'"
        for x in quitar:
            self.texto = self.texto.replace(x, '')
        self.texto = self.texto.lower()
        palabras = self.texto.split(' ')

        dicc = {}
        for x in palabras:
            if x in dicc:
                dicc[x] += 1
            else:
                dicc[x] = 1
        for x in dicc:
            frecuency = dicc[x]
            print(f'La palabra "{x}" tiene una frecuencia de {frecuency}')


if __name__ == '__main__':
    texto = Frecuencia('Hola, mundo. Esto es una cadena, se supone que debe tener varias palabras pues  vamos a realizar un conteo de frecuencia de las mismas usando el lenguaje de programación Python.  Ya no sé qué escribir pero sigo escribiendo para que poco a poco la cadena sea más larga y el  ejercicio de programación sea demostrable. Creo que con todo esto que he escrito es suficiente')
    print(texto.generar())
