import modulo

def vérticesAdj(matriz):
    colors={
        'azul':'\033[1;34m',
        'roxo':'\033[1;95m',
        'amar':'\033[1;93m',
        'zera':'\033[0;0m'
    }
    print(f'O grafo tem {colors["azul"]}{len(matriz)}{colors["zera"]} vértices.')
    vet=int(input('Digite o vértice que deseja verificar: '))
    cont=0
    for item in matriz[vet-1]:
        if item==1:
            cont+=1
    print(f'O {colors["amar"]}vertice {vet}{colors["zera"]} tem {colors["roxo"]}{cont} vértices adjacentes{colors["zera"]}')

if __name__ == "__main__":
    matriz = modulo.retornaMatriz()
    vérticesAdj(matriz)