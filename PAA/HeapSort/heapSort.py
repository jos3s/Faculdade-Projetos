import modulo as mod
import sys

if __name__ == '__main__':
    entrada=open(sys.argv[1],"r")
    saida=open(sys.argv[2], "w")
    vetor=[]

    for valor in entrada:
        vetor.append(int(valor))

    nLinhas,vetor=mod.heapsort(vetor)
    saida.write(str(nLinhas))
    saida.write('\n')

    for pos in range(nLinhas):
        saida.write(str(vetor[pos]))
        if pos<nLinhas-1: saida.write('\n')

    saida.close()
    entrada.close()
