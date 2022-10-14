with open('2input.txt') as file:
    linhas = file.read().splitlines()

numeroDeSenhasValidas = 0

for linha in linhas:
    campos = linha.split()

    letraNecessariaDaSenha = campos[1][0]
    senha = campos[2]
    intervalo = campos[0].split('-')
    intervalo = list(map(int, intervalo))

    numeroDeOcorrencias = senha.count(letraNecessariaDaSenha)

    indiceInferior = intervalo[0]
    indiceSuperior = intervalo[1]

    if (senha[indiceInferior-1] == letraNecessariaDaSenha) ^ (senha[indiceSuperior-1] == letraNecessariaDaSenha):
        numeroDeSenhasValidas += 1

print(numeroDeSenhasValidas)
