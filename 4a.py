with open('4input.txt') as file:
    stringsPassaporte = file.read().split('\n\n')

listaDePassaportes = []

for linhasPassaporte in stringsPassaporte:
    linhas = linhasPassaporte.splitlines()
    passaporte = {}
    for linha in linhas:
        campos = linha.split()
        for campo in campos:
            nomeDoCampo, valor = campo.split(':')
            passaporte[nomeDoCampo] = valor
    listaDePassaportes.append(passaporte)

camposObrigatorios = ('byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid')

numeroDePassaportesValidos = 0

for passaporte in listaDePassaportes:
    contemTodosOsCamposValidos = True
    for campoObrigatorio in camposObrigatorios:
        if campoObrigatorio not in passaporte:
            contemTodosOsCamposValidos = False
    if contemTodosOsCamposValidos:
        numeroDePassaportesValidos += 1

print(numeroDePassaportesValidos)
