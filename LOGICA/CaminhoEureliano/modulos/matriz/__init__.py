def lerArq():
	try:
		arq=open('LOGICA\CaminhoEureliano\entrada.txt','r',encoding="utf8")
	except:
		print('Erro na leitura do arquivo')
	else:
		entrada=[]
		for linha in arq:
			itens=linha.rstrip('\n').strip(' ').split(' ')
			entrada.append([int(itens[0]),int(itens[1])])
		return entrada


def criarMatriz():
	entrada=lerArq()
	passos=int(len(entrada)/2)
	matriz=[]
	valor=1
	for _ in entrada:
		l=[]
		for _ in range (0,passos):
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


def passos():
	matriz=criarMatriz()
	passos=[]
	for i in range(len(matriz)):
		passos.append(matriz[i][0])
	return passos
