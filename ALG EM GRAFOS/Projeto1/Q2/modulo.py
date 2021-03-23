def lerArq(tipo):
    try:
        if 'norientado' in tipo:
            a = open('norientado.txt', 'rt')
        else:
            a = open('orientado.txt', 'rt')
    except:
        print('Erro na leitura do arquivo')
    else:
        matriz = []
        for linha in a:
            linha = linha.split(' ')
            matriz.append(linha)
        return matriz


def limparMatriz(m):
    matriz = []
    for lista in m:
        linha = []
        for item in lista:
            linha.append(item.rstrip('\n'))
        matriz.append(linha)
    return matriz


def criarMatrizAdjacencia(info):
    matriz = []
    for i in range(0, int(info[0])):
        lista = []
        for i in range(0, int(info[0])):
            lista.append(0)
        matriz.append(lista)
    return matriz


def matrizAdjacencia(info, dados):
    matriz = criarMatrizAdjacencia(info)
    tam = len(matriz[0])
    if info[2] in 'Dd':
        for linha in dados:
            for i in range(0, tam):
                if i == int(linha[1])-1:
                    matriz[int(linha[0])-1][i] = -1
                    matriz[i][int(linha[0])-1] = 1
    else:
        for linha in dados:
            for i in range(0, tam):
                if i == int(linha[1])-1:
                    matriz[int(linha[0])-1][i] = int(linha[2])
                    matriz[i][int(linha[0])-1] = int(linha[2])
    return matriz


def retornaMatriz(tipo):
    matriz = lerArq(tipo)
    matrizArq = limparMatriz(matriz)
    info = matrizArq.pop(0)
    return matrizAdjacencia(info, matrizArq)

