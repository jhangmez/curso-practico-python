class ComunDivisor:
    def __init__(self, numero, numero1):
        self.numero = numero
        self.numero1 = numero1

    def maximo(self):
        while (self.numero1):
            self.numero, self.numero1 = self.numero1, self.numero % self.numero1
        return self.numero

    def minimo(self):
        return (self.numero*self.numero1)/self.maximo(self.numero1)


if __name__ == '__main__':
    numero = ComunDivisor(124, 6)

    print(numero.maximo())
    print(numero.minimo())
