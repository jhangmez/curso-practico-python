# def conversacion(mensaje):
#     print('Hola')
#     print('Cómo estás')
#     print('Elegiste la opcion '+mensaje)
#     print('Adios')


# opcion = int(input('Elige una opción (1, 2, 3): '))
# try:
#     if opcion == 1:
#         conversacion('1')
#     elif opcion == 2:
#         conversacion('2')
#     elif opcion == 3:
#         conversacion('3')
#     else:
#         print('Escribe la opción correcta')
# except ValueError:
#     print('Ocurrio un error')

# for contador in range(44, 1000):
#     contador += 1
#     print(13*contador)

def run():
    paises_capital = {
        'Peru': 'Lima',
        'Argentina': 'Buenos Aires',
        'Paraguay': 'Montevideo'
    }
    pais = input('Escriba el pais: ')
    print('La capital del '+pais+' es '+ paises_capital[pais])
    # print(paises_capital.get('Paraguay'))
 


if __name__ == '__main__':
    run()