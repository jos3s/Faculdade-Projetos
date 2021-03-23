def construirHeap(vet, n, idPai):
    maior=idPai
    esq=2*idPai+1
    dir=2*idPai+2

    if esq<n and vet[esq]>vet[maior]:
        maior = esq
    if dir<n and vet[dir]>vet[maior]:
        maior = dir
    if maior!=idPai:
        vet[maior],vet[idPai]=vet[idPai],vet[maior]
        construirHeap(vet, n, maior)

def heapsort(vet):
    nLinhas=vet[0]
    del vet[0]
    
    for i in range(nLinhas // 2 -1, -1, -1):
        construirHeap(vet, nLinhas, i)

    for i in range(nLinhas-1, 0, -1):
        vet[i], vet[0] = vet[0], vet[i]
        construirHeap(vet, i, 0)

    return nLinhas, vet
