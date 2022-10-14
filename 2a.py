with open('2input.txt') as file:
    linhas = file.read().splitlines()

numeroDeSenhasValidas = 0

for linha in linhas:
    campos = linha.split()

    letraNecessariaDaSenha = campos[1][0]
    senha = campos[2]
    intervalo = list(map(int, campos[0].split('-')))

    numeroDeOcorrencias = senha.count(letraNecessariaDaSenha)

    limiteInferior = intervalo[0]
    limiteSuperior = intervalo[1]

    if limiteInferior <= numeroDeOcorrencias <= limiteSuperior:
        numeroDeSenhasValidas += 1

print(numeroDeSenhasValidas)
