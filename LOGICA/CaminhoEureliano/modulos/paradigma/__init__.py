from pysat.solvers import Glucose4
from pysat.formula import CNF
from math import ceil
from modulos.matriz import criarMatriz, lerArq, passos

#Variaveis globais
matriz = criarMatriz()
arestas = lerArq()
numPassos = passos(arestas)

def resolver(passo:int,conjuntoVertices:bool=False,ordemVertices:bool=True):
	"""Resolve o caminho eureliano do grafo.

	:param passo: Recebe um array contendo os primeiros passos de cada possível começo do problema
	:param conjuntoVertices: Exibir o uma lista fora de ordem com o conjunto dos vértices que resolvem o problema. (Default value = False)
	:param ordemVertices: Exibir o caminho pelos vértices a ser percorrido para resolver o problema. (Default value = True)

 	"""
	formula=CNF()
	g=Glucose4()
	getClausulas(matriz,formula)
	formula.append([passo])
	g.append_formula(formula)
	print(f'O passo inicial para prova é: \33[32m{passo}\33[m, o caminho com ele é \33[34m{g.solve()}\33[m')
	model=g.get_model()
	if model:
		valoracaoValida = valoresValidos(model)
		print(f'Passos válidos: \33[35m{valoracaoValida}\33[m')
		if conjuntoVertices:
			print(f'Esse são os conjuntos de vértices usados (fora de ordem): \33[36m{caminhosUsados(model)}\33[m')
		if ordemVertices:
			print(f"Ordem de passagem pelos vértices: ")
			printEmOrdem(valoracaoValida)
	print()


def printEmOrdem(passos:list):
	lista = verticesEmOrdem(passos)
	print('\33[33m[', end='')
	for i in range(0, len(lista)):
		print(lista[i], end='')
		if i != len(lista)-1:
			print(' -> ', end='')
	print(']\33[m')


def verticesEmOrdem(passos:list):
	ordenados = []
	tam = len(passos)
	for _ in range(0, tam+1):
		ordenados.append(-1)

	for passo in passos:
		iAresta = int((passo-1)/tam)
		ar = arestas[iAresta][0]
		iOrdenados = -1
		while (int((passo-1)/tam)) == iAresta and passo > 0:
			iOrdenados += 1
			passo -= 1
		ordenados[iOrdenados] = ar
		if iOrdenados == (len(ordenados)-2):
			iOrdenados += 1
			ar = arestas[iAresta][1]
			ordenados[iOrdenados] = ar

	return ordenados


def getClausulas(matriz:list[list], formula:CNF, lin:int=0, col:int=0):
	for col in range(len(matriz[lin])):
		for lin in range(len(matriz)):
			for auxCol in range(col+1, len(matriz[lin])):
				formula.append([-matriz[lin][col], -matriz[lin][auxCol]])
			auxForm = [-matriz[lin][col]]
			for auxLin in range(len(matriz)):
				if auxLin != lin:
					formula.append([-matriz[lin][col], -matriz[auxLin][col]])
				if arestas[lin][0] == arestas[auxLin][1] and arestas[lin][1] == arestas[auxLin][0]:
					negarLinha(matriz[lin][col], auxLin, col+1, matriz, formula)
				if arestas[lin][1] == arestas[auxLin][0] and col < len(matriz[lin])-1:
					auxForm.append(matriz[auxLin][col+1])
			if len(auxForm) > 1:
				formula.append(auxForm)


def negarLinha(valor:int, lin:int, col:int, matriz:list[list], formula:CNF):
	for col in range(col, len(matriz[lin])):
		formula.append([-valor, -matriz[lin][col]])


def valoresValidos(model:list):
	if model:
		return list(filter(lambda x: x>0, model ))


def calcularPosicao(passos:list):
	pos=[]
	for item in passos:
		pos.append(int(ceil(item/numPassos))-1)
	return pos


def retornarIdxVertices(model:list):
	if model:
		a=list(filter(lambda x: x>0, model ))
		return calcularPosicao(a)


def caminhosUsados(model:list)-> list:
	pos=retornarIdxVertices(model)
	vet=[]
	for item in pos:
		vet.append(arestas[item])
	return vet
