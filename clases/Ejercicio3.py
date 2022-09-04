class Factorial:
    def __init__(self, numero):
        self.numero = numero

    def multiplicar(self):
        if self.numero < 0:
            return f'{self.numero} es un numero negativo'
        elif self.numero == 0:
            return 1
        else:
            fact = 1
            while (self.numero > 1):
                fact *= self.numero
                self.numero -= 1
            return fact


if __name__ == '__main__':
    Numero = Factorial(9)
    print(Numero.multiplicar())
