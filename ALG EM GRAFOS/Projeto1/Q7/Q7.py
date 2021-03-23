import random

def criaLista(vet):
    lista=[]
    for i in range(0,vet):
        lista.append([])
    return lista


def cicloOuConexo(vet):
    lista=criaLista(vet)
    vetr=1
    for i in range(0,vet):
        if i == vet-1:
            lista[i].append([vetr,1])
        else:
            lista[i].append([vetr,vetr+1])
            vetr+=1
    salvaArq(lista,len(lista))
    

def completo(vet):
    lista=criaLista(vet)
    valor=1
    for v in range(0,vet):
        for i in range(valor,vet):
            lista[v].append([v+1,i+1])
        valor+=1
    salvaArq(lista,len(lista))


def bipartido(vet, n):
    parte1=criaLista(n)
    parte2=criaLista(vet-n)
    for i in range(0,len(parte2)):
        for linha in parte1:
            linha.append(i)
    lista=[]
    for i in range(0, len(parte1)):
        for j in range(0,len(parte1[i])):
            if i==0:
                lista.append([[1,(parte1[0][j]+len(parte1))+1]])
            elif random.randrange(0,len(parte1)) %2==0:
                lista.append([[i+1,(parte1[i][j]+len(parte1))+1]])
    salvaArq(lista,vet)


def salvaArq(lista, tam):
    colors = { 'verde':'\033[1;92m', 'verm':'\033[1;91m', 'zera':'\033[0;0m' }
    try:    
        a = open('saida.txt', 'w')
    except:
        print(f'{colors["verm"]} Erro na gravação do arquivo {colors["zera"]}')
    else:
        a.write(f"{tam} {len(lista)} G \n")
        for linha in lista:
            for lista in linha:
                a.write(f'{lista[0]} {lista[1]} 1 \n')  
        print(f'{colors["verde"]} Arquivo salvo com sucesso, veja o arquivo "saida.txt" {colors["zera"]}') 


if __name__ == "__main__":
    colors={
        'verde'  : '\033[1;32m', 'azul'  : '\033[1;94m', 'roxo': '\033[1;95m',
        'amar'   : '\033[1;93m', 'verm'  : '\033[1;91m', 'cyan': '\033[1;36m',
        'magenta': '\033[1;35m', 'branco': '\033[1;97m', 'zera': '\033[0;0m'
    }
    num=True
    while num:
        vet=input(f' Digite o {colors["branco"]}numero de vértices{colors["zera"]} do grafo não orientado: ')
        try:
            vet=int(vet)
            num=False
        except:
            print(f' {colors["verm"]}Você precisa digitar um número. {colors["zera"]}')
            num=True
    while True:
        print()
        print(f' {colors["amar"]}a.{colors["zera"]} Grafo {colors["verde"]}Ciclo{colors["zera"]}')
        print(f' {colors["amar"]}b.{colors["zera"]} Grafo {colors["cyan"]}Conexo{colors["zera"]}')
        print(f' {colors["amar"]}c.{colors["zera"]} Grafo {colors["roxo"]}Completo{colors["zera"]}')
        print(f' {colors["amar"]}d.{colors["zera"]} Grafo {colors["azul"]}Bipartido{colors["zera"]}') 
        opc=input(" Digite a letra correspondente a sua escolha: ")
        if opc in 'Aa':
            print(f'\n Você escolheu:{colors["verde"]} Grafo Ciclo {colors["zera"]}')
            cicloOuConexo(vet)
            break
        elif opc in 'Bb':
            print(f'\n Você escolheu:{colors["cyan"]} Grafo Conexo {colors["zera"]}')
            cicloOuConexo(vet)
            break
        elif opc in 'Cc':
            print(f'\n Você escolheu:{colors["roxo"]} Grafo Completo {colors["zera"]}')
            completo(vet)
            break
        elif opc in 'Dd':
            print(f'\n Você escolheu:{colors["azul"]} Grafo Bipartido {colors["zera"]}')
            if vet <2:
                print(f' Esse grafo {colors["verm"]}não poder ser bipartido {colors["zera"]}')
                continue
            n=int(input(" Digite o numero de vértices na 1 partição: "))
            if n>=vet:
                print(f' O valor da 1 partição {colors["verm"]}não pode ser maior que o número de grafos{colors["zera"]}')
                continue
            bipartido(vet,n)
            break
        else: 
            print(f' {colors["verm"]}Opção inválida{colors["zera"]}')
            continue
