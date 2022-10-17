def numeroDeArvoresQuandoSeDesceNoAngulo(angulo):
    variacaoHorizontal, variacaoVertical = angulo

    numeroDeArvores = 0
    posicaoHorizontal = 0

    for posicaoVertical in range(0, len(mapa), variacaoVertical):
        linha = mapa[posicaoVertical]
        tamanhoDalinha = len(linha)
        if linha[posicaoHorizontal % tamanhoDalinha] == '#':
            numeroDeArvores += 1
        posicaoHorizontal += variacaoHorizontal

    return numeroDeArvores


with open('3input.txt') as file:
    mapa = file.read().splitlines()

angulos = ((1, 1), (3, 1), (5, 1), (7, 1), (1, 2))
multiplicacaoDoNumeroDeCadaAngulo = 1

for angulo in angulos:
    multiplicacaoDoNumeroDeCadaAngulo *= numeroDeArvoresQuandoSeDesceNoAngulo(angulo)

print(multiplicacaoDoNumeroDeCadaAngulo)
