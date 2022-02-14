import modulo

def matrizNaoOrientada(matriz):
    max=[None,0]
    min=[None,0]
    numMaiorZero=[x for x in matriz[0] if x != 0]
    cont=len(numMaiorZero)   
    max[0]=min[0]=cont
    
    for i in range(0,len(matriz[0])):
        numMaiorZero=[x for x in matriz[i] if x != 0]
        cont=len(numMaiorZero)   
        if cont>max[0]:
            max[0]=cont
            max[1]=i+1
        if cont<min[0]:     
            min[0]=cont
            min[1]=i+1            
    colors={
        'verde': '\033[1;32m', 'verm': '\033[1;91m', 'zera': '\033[0;0m'
    }  
    print(f' O vértice com {colors["verde"]}maior grau é o {max[1]} {colors["zera"]} ')
    print(f' O vértice com {colors["verm"]}menor grau é o {min[1]} {colors["zera"]} ')
    

def matrizOrientada(matriz):
    colors={
        'verde': '\033[1;32m', 'verm': '\033[1;91m', 'magenta':'\033[1;95m', 'zera':'\033[0;0m'
    }
    entrada = 0
    saida = 0
    nLinha=1
    for linha in matriz:
        for item in linha:
            if int(item)==-1:
                saida+=1
            elif int(item)==1:
                entrada+=1
        print(f' O {colors["magenta"]}vértice {nLinha}{colors["zera"]} tem grau {colors["verm"]}{saida} de saida{colors["zera"]} e {colors["verde"]}{entrada} de entrada{colors["zera"]}')
        saida=entrada=0
        nLinha+=1


if __name__ == "__main__":
    colors={
        'roxo':'\033[1;95m', 'amar':'\033[1;93m', 'zera':'\033[0;0m'
    }
    op=int(input(f' Digite {colors["roxo"]}1  para um grafo orientado{colors["zera"]} e {colors["amar"]}2 para não orientado{colors["zera"]}: '))
    if op==1:
        matriz = modulo.retornaMatriz('orientado')
        matrizOrientada(matriz)
    else:
        matriz = modulo.retornaMatriz('norientado')
        matrizNaoOrientada(matriz)
        