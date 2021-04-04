def lerArq():
	try:
		arq=open('entrada.txt','rt',encoding="utf8")
	except:
		print('Erro na leitura do arquivo')
	else:
		entrada=[]
		for linha in arq:
			itens=linha.rstrip('\n').strip(' ').split(' ')
			entrada.append([int(itens[0]),int(itens[1])])
		return entrada


def criarMatriz():
	arestas=lerArq()
	pass0s= passos(arestas)
	matriz=[]
	valor=1
	for _ in arestas:
		l=[]
		for _ in range (0,pass0s):
			l.append(valor)
			valor+=1
		matriz.append(l)
	return matriz


def printMatriz(matriz):
	arestas=lerArq()
	for i in range(len(matriz)):
		print(f"{arestas[i]} [",end="")
		for j in range(len(matriz[i])):
			print(f"\33[34m{matriz[i][j]}{' ' if j<(len(matriz[i])-1) else ''}", end="")
		print("\33[m]")


def primeirosPassos():
	matriz=criarMatriz()
	passos=[]
	for i in range(len(matriz)):
		passos.append(matriz[i][0])
	return passos


def passos(arestas):
    return int(len(arestas)/2)
