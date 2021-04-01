from pysat.solvers import Glucose4
from pysat.formula import CNF


def lerArq():
    try:
        arq=open('entrada.txt','r',encoding="utf8")
    except:
        print('Erro na leitura do arquivo')
    else:
        entrada=[]
        for linha in arq:
            itens=linha.rstrip('\n').strip(' ').split(' ')
            entrada.append([int(itens[0]),int(itens[1])])
        return entrada
    
 
def criarMatriz(entrada):
    passos=int(len(entrada)/2)
    matriz=[]
    valor=1
    for linha in entrada:
        l=[]
        for i in range (0,passos):
            l.append(valor)
            valor+=1
        matriz.append(l)
    return matriz


def printMatriz(matriz):
    for linha in matriz:
        print(linha)