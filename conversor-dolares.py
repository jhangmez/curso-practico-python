def convertir(dolares, cantidad):
    convertido = dolares*cantidad
    # print(convertido)
    return convertido
    


def run():
    tipomoneda_pais = {
        'peru': 'Soles',
        'argentina': 'Pesos argentinos',
        'Ecuador': 'Dolares',
        'Brasil': 'Real brasileno'
    }
    tipocambio_pais = {
        'peru': 3.73,
        'argentina': 109.41,
        'Ecuador': 1,
        'Brasil': 5.08
    }
    pais = input('Escriba el pais: ')
    dolares = float(input('Cuantos dolares quiere convertir: '))
    #moneda = tipomoneda_pais[pais]
    # cantidad = tipocambio_pais[pais]
    #print(moneda)
    totalconvertido = convertir(dolares, tipocambio_pais[pais])
    # print(totalconvertido)
    print(f'El tipo de cambio de {pais} con su moneda {tipomoneda_pais[pais]}')
    print(f'La cantidad fue {dolares} y su conversion es {totalconvertido}')

if __name__ == '__main__':
    run()
