def lerArq(nomeArq):
    try:
        a = open(nomeArq, 'rt')
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
    matriz=adicionarIndices(matriz)
    return matriz


def adicionarIndices(matriz):
    tam = len(matriz[0])
    lista = []
    for i in range(1, tam+1):
        lista.append(i)
    matriz.insert(0, lista)
    i = 0
    for linha in matriz:
        linha.insert(0, i)
        i += 1
    return matriz


def criarMatrizIncidencia(info):
    matriz = []
    for i in range(0, int(info[0])):
        lista = []
        for i in range(0, int(info[1])):
            lista.append(0)
        matriz.append(lista)
    return matriz


def matrizIncidencia(info,dados):
    matriz = criarMatrizIncidencia(info)
    if info[2] in 'Gg':
        tam = len(matriz[0])
        i=0
        for linha in dados:
            matriz[int(linha[0])-1][i] = 1
            matriz[int(linha[1])-1][i] = 1
            i+=1        
    else:
        tam = len(matriz[0])
        i=0
        for linha in dados:
            matriz[int(linha[0])-1][i] = -1
            matriz[int(linha[1])-1][i] = 1
            i+=1    
    matriz=adicionarIndices(matriz)
    return matriz
        

if __name__ == "__main__":
    colors={
        'verde': '\033[1;32m', 'azul': '\033[1;34m', 'roxo': '\033[1;95m', 'amar': '\033[1;93m', 'zera': '\033[0;0m'
    }
    print(f' Digite {colors["roxo"]}1 para o Grafo Não Orientado {colors["zera"]} ou {colors["amar"]} 2 para o Grafo Orientado {colors["zera"]}')
    op=int(input(' Qual a sua escolha: ' ))
    if op==1:
        dados = lerArq('entrada.txt')
    else:
        dados = lerArq('ent2.txt')
    matrizArq = limparMatriz(dados)
    info = matrizArq.pop(0)
    esc = int(input(f' Digite {colors["azul"]} 1 para Matriz de Adjacencia {colors["zera"]} ou {colors["verde"]} 2 para Matriz de Incidencia: {colors["zera"]}'))
    if esc == 1:
        matriz = matrizAdjacencia(info, matrizArq)
        for linha in matriz:
            print(f'{colors["azul"]} {linha} {colors["zera"]}  ')
    else:
        matriz = matrizIncidencia(info, matrizArq)
        for linha in matriz:
            print(f'{colors["verde"]} {linha} {colors["zera"]}  ')