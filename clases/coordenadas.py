# definicion de clases
class Coordenada:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def distancia(self, otracoordenada):
        x_diff = (self.x-otracoordenada.x)**2
        y_diff = (self.y-otracoordenada.y)**2

        return f'{(x_diff-y_diff)**2} m'


if __name__ == '__main__':
    Coordenada1 = Coordenada(12, 14)
    Coordenada2 = Coordenada(158, 166)

    print(Coordenada1.distancia(Coordenada2))
