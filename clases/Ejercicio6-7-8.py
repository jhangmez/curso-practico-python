class RecibeLista:
    def __init__(self, lista):
        self.lista = lista

    def media(self):
        valormedia = sum(self.lista)/len(self.lista)
        return valormedia

    def cuadrados(self):
        valorcuadrados = [x**2 for x in self.lista]
        return valorcuadrados

    def varianza(self):
        sumatoriavarianza = 0
        for x in self.lista:
            sumatoriavarianza += (x-self.media())**2
        return round(sumatoriavarianza/len(self.lista), 2)

    def desviacionestandar(self):
        return round(self.varianza()**0.5, 2)

    def diccionario(self):
        dicc = {}
        dicc['Media'] = self.media()
        dicc['Varianza'] = self.varianza()
        dicc['Desviacion'] = self.desviacionestandar()

        return dicc


if __name__ == '__main__':
    ValorLista = [11, 15, 17, 18]
    resultado = RecibeLista(ValorLista)
    #print(f'El resultado de la media es: {resultado.media()}')
    #print(f'Los valores de la lista todos al cuadrado quedaria de la siguiente forma: {resultado.cuadrados()}')
    #print(f'El resultado de la varianza es: {resultado.varianza()}')
    #print(f'El resultado de la desviacion estandar es: {resultado.desviacionestandar()}')
    print(resultado.diccionario())
