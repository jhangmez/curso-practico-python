class Conversion:
    def __init__(self, numero):
        self.numero = numero

    def binario(self):
        conversionbinario = format(self.numero, 'b')
        return conversionbinario
        # Retorna pero en str/bin

    def decimal(self):
        conversiondecimal = 0
        for x in self.binario():
            conversiondecimal = conversiondecimal*2 + int(x)
        return conversiondecimal


if __name__ == '__main__':
    numero = Conversion(25)

    print(numero.binario())
    print(numero.decimal())
