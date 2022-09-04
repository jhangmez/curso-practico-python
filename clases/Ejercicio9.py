class ComunDivisor:
    def __init__(self, numero):
        self.numero = numero

    def maximo(self, numero1):
        if (self.numero > numero1):
            menor = numero1
        else:
            menor = self.numero
        for i in range(1, menor+1):
            if (self.numero % i == 0) and (numero1 % i == 0):
                max = i
        return max

    def minimo(self, numero1):
        return (self.numero*numero1)/self.maximo(numero1)


if __name__ == '__main__':
    numero = ComunDivisor(124)

    print(numero.maximo(6))
    print(numero.minimo(6))
