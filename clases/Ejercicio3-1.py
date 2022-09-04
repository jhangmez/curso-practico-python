class Factorial:
    def __init__(self, numero):
        self.numero = numero

    def multiplicar(self):
        return 1 if (self.numero == 1 or self.numero == 0) else self.numero * self.multiplicar(self.numero - 1)


if __name__ == '__main__':
    Numero = Factorial(6)
    print(Numero.multiplicar())
