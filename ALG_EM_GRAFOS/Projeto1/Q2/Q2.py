import modulo

def lista(matriz):
    tam = len(matriz)
    listaAdj = []
    for i in range(0, tam):
        lista = []
        listaAdj.append(lista)
    return listaAdj


def criarListaAdj(matriz, tipo):
    ls = lista(matriz)
    if tipo == 'norientado':
        for i in range(0, len(ls)):
            for j in range(0, len(matriz[0])):
                if matriz[i][j] != 0:
                    ls[i].append(j+1)
    else:
        for linha in matriz:
            print(linha)
        for i in range(0,len(ls)):
            for j in range(0,len(matriz[0])):
                if matriz[i][j]==-1:
                    ls[i].append(j+1)
    return ls




if __name__ == "__main__":
    colors={
        'verde':'\033[1;32m','negrito':'\033[;1m', 'roxo':'\033[1;95m', 
        'amar':'\033[1;93m', 'zera':'\033[0;0m'
    }
    op=int(input(f'Digite {colors["roxo"]}1 para um grafo orientado{colors["zera"]} e {colors["amar"]}2 para não orientado:{colors["zera"]} '))
    if op==1:
        matriz = modulo.retornaMatriz('orientado')
        listaAdj = criarListaAdj(matriz,'orientado')
    else:
        matriz = modulo.retornaMatriz('norientado')
        listaAdj = criarListaAdj(matriz,'norientado')
    print(f'{colors["negrito"]} Lista de adjacência')
    for i in range(0, len(listaAdj)):
        print(f'{colors["roxo"]} {i+1} {colors["amar"]} {listaAdj[i]} {colors["zera"]}')