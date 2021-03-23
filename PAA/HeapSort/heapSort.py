import modulo as mod

if __name__ == '__main__':
    entrada=open("entrada.txt","r")
    saida=open("saida.txt", "w")
    vetor=[]

    for valor in entrada:
        vetor.append(int(valor))

    nLinhas,vetor=mod.heapsort(vetor)
    saida.write(str(nLinhas))
    saida.write('\n') 

    for pos in range(nLinhas):
        saida.write(str(vetor[pos]))
        saida.write('\n')

    saida.close()
    entrada.close()
