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
numeroDePassaportesValidosECorretos = 0
passaportesValidos = []

for passaporte in listaDePassaportes:
    contemTodosOsCamposValidos = True
    for campoObrigatorio in camposObrigatorios:
        if campoObrigatorio not in passaporte:
            contemTodosOsCamposValidos = False
    if contemTodosOsCamposValidos:
        passaportesValidos.append(passaporte)

for passaporte in passaportesValidos:
    temTodosOsValoresCorretos = True
    for chave, valor in passaporte.items():
        if chave == 'byr':
            ano = int(valor)
            if ano < 1920 or ano > 2002:
                temTodosOsValoresCorretos = False
        elif chave == 'iyr':
            ano = int(valor)
            if ano < 2010 or ano > 2020:
                temTodosOsValoresCorretos = False
        elif chave == 'eyr':
            ano = int(valor)
            if ano < 2020 or ano > 2030:
                temTodosOsValoresCorretos = False
        elif chave == 'hgt':
            unidade = valor[-2:]
            if unidade != 'cm' and unidade != 'in':
                temTodosOsValoresCorretos = False
            try:
                altura = int(valor[:-2])
                if unidade == 'cm':
                    if altura < 150 or altura > 193:
                        temTodosOsValoresCorretos = False
                if unidade == 'in':
                    if altura < 59 or altura > 76:
                        temTodosOsValoresCorretos = False
            except:
                temTodosOsValoresCorretos = False
        elif chave == 'hcl':
            if valor[0] != '#' or len(valor) != 7:
                temTodosOsValoresCorretos = False
            else:
                try:
                    int(valor[-6:], 16)
                except:
                    temTodosOsValoresCorretos = False
        elif chave == 'ecl':
            coresPossiveis = ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']
            if valor not in coresPossiveis:
                temTodosOsValoresCorretos = False
        elif chave == 'pid':
            if len(valor) != 9:
                temTodosOsValoresCorretos = False
            try:
                int(valor)
            except:
                temTodosOsValoresCorretos = False
    if temTodosOsValoresCorretos:
        numeroDePassaportesValidosECorretos += 1

print(numeroDePassaportesValidosECorretos)
