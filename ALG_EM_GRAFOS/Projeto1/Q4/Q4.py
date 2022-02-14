import modulo

def grafoRegular(matriz):
    repetidos = []
    for linha in matriz:
        cont=0
        for i in linha:
            if i==1:
                cont+=1
        repetidos.append(cont)
    retorno = False
    for valor in repetidos:
        if repetidos[0]==valor:
            retorno=True
        else: 
            retorno=False
            break
    
    return retorno


if __name__ == "__main__":
    colors={
        'verde':'\033[1;32m',
        'verm':'\033[1;91m',
        'zera':'\033[0;0m'
    }  
    matriz = modulo.retornaMatriz()
    retorno=grafoRegular(matriz)
    if retorno:
        print(f'O grafo é regular: {colors["verde"]} {retorno}{colors["zera"]}')
    else:
        print(f'O grafo é regular: {colors["verm"]} {retorno}{colors["zera"]}')