import random


def generar_contrasena():
    mayusculas = ['A', 'B', 'C', 'D', 'E', 'F', 'G']
    minusculas = ['a', 'b', 'c', 'd', 'e', 'f', 'g']
    simbolos = ['!', '@', '#', '$', '%', '^', '&']
    numeros = ['1', '2', '3', '4', '5', '6', '7', '8', '9']

    caracteres = mayusculas + minusculas + simbolos + numeros

    

    for i in range(15):
        caracter_random = random.choice(caracteres) # metodo de random para elegir un elemento al azar de la lista.
        contrasena.append(caracter_random)

    contrasena = ''.join(contrasena) # transforma listas en strigns.
    return contrasena


def run():
    contrasena = generar_contrasena()
    print(f'Tu nueva contrasena es: {contrasena}')


if __name__ == '__main__':
    run()