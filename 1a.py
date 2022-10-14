with open('1input.txt') as file:
    listaDosNumeros = file.read().splitlines()
    listaDosNumeros = list(map(int, listaDosNumeros))

resultado = [elemento1 * elemento2
             for elemento1 in listaDosNumeros
             for elemento2 in listaDosNumeros
             if elemento1 + elemento2 == 2020]

print(resultado[0])
