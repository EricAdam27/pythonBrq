with open('3input.txt') as file:
    mapa = file.read().splitlines()

numeroDeArvores = 0
posicaoHorizontal = 0

for linha in mapa:
    tamanhoDalinha = len(linha)
    if linha[posicaoHorizontal % tamanhoDalinha] == '#':
        numeroDeArvores += 1
    posicaoHorizontal += 3

print(numeroDeArvores)
