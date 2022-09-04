class AreaVolumen:
    def __init__(self, radio):
        self.radio = radio

    def area(self):
        return 3.1415 * self.radio*self.radio

    def volumen(self, altura):
        return self.area() * altura


if __name__ == '__main__':
    Circulo = AreaVolumen(3)

    print(Circulo.area())
    print(Circulo.volumen(4))
