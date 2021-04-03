from modulos.paradigma import resolver
from modulos.matriz import passos, printMatriz,criarMatriz

if __name__ == '__main__':
    while True:
        opc=input("Deseja exibir a matriz de passos? [S/n]")
        if opc in 'Ss':
            printMatriz(criarMatriz())
            break
        else:
            break
    print("\nExecutando o caminho eureliano: ")
    passo = passos()
    for item in passo:
        resolver(item)
