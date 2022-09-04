class Porcentaje:
    def __init__(self, iva, cantidad):
        self.iva = iva
        self.cantidad = cantidad

    def porcentaje(self):
        valortotal = self.cantidad*(1+self.iva/100)
        return f'La cantidad asignada es S/ {self.cantidad} y el iva es de {self.iva}%, y el valor total es S/ {valortotal}'


if __name__ == '__main__':
    ValorCantidad = Porcentaje(21, 1000)
    print(ValorCantidad.porcentaje())
