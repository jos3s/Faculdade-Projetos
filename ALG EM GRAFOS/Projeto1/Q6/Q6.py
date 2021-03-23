# This Python file uses the following encoding: utf-8 
def lista():
    colors={
        'azul':'\033[1;34m',
        'zera':'\033[0;0m'
    }
    tam = int(input(f' Qual a {colors["azul"]}quantidade de vértices{colors["zera"]} de grafo: '))
    listaAdj = []
    for i in range(0, tam):
        lista = []
        listaAdj.append(lista)
    return listaAdj


def criarListaAdj():
    colors={
        'verde':'\033[1;32m',
        'zera':'\033[0;0m'
    }
    ls = lista()
    for i in range(0, len(ls)):
        grafo = str(i+1)
        opc = int(input(f' Digite a {colors["verde"]}quantidade de vértices adjacentes{colors["zera"]} ao grafo '+grafo+': '))
        
        while opc != 0:
            ls[i].append(1)
            opc -= 1
    return ls


def vérticesAdj(lista):
    colors={
        'roxo':'\033[1;95m',
        'amar':'\033[1;93m',
        'verm':'\033[1;91m',
        'zera':'\033[0;0m'
    }
    esc = (int(input(' Digite o vertice? ')))
    if esc>len(lista):
        print(f" {colors['verm']}Valor inválido{colors['zera']}")
        vérticesAdj(lista)
    else:
        tam = len(lista[esc-1])
        print(f' O {colors["amar"]}vertice {esc}{colors["zera"]} tem {colors["roxo"]}{tam} vértices adjacente{colors["zera"]}')

if __name__ == "__main__":
    ls = criarListaAdj()
    vérticesAdj(ls)
