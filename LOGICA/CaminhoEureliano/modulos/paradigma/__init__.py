from pysat.solvers import Glucose4
from pysat.formula import CNF
from math import ceil
from modulos.matriz import criarMatriz, lerArq, passos

#Variaveis globais
matriz=criarMatriz()
arestas=lerArq()
numPassos=passos(arestas)

def getPdgs(matriz, formula, lin=0, col=0):
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


def negarLinha(valor, lin, col, matriz, formula):
	for col in range(col, len(matriz[lin])):
		formula.append([-valor, -matriz[lin][col]])

def resolver(passo,conjuntoVertices=False,ordemVertices=True):
	"""Resolve o caminho eureliano do grafo.

	Args:
		passo (int): Recebe um array contendo os primeiros passos de cada possível começo do problema
		conjuntoVertices (bool, optional): Exibir o uma lista fora de ordem com o conjunto dos vértices que resolvem o problema. Padrão é False.
		ordemVertices (bool, optional): Exibir o caminho pelos vértices a ser percorrido para resolver o problema. Padrão é True.
 	"""
	formula=CNF()
	g=Glucose4()
	getPdgs(matriz,formula)
	formula.append([passo])
	g.append_formula(formula)
	print(f'O passo inicial para prova é:\33[32m{passo}\33[m, o caminho com ele é \33[34m{g.solve()}\33[m')
	model=g.get_model()
	if model:
		vetor=valoresValidos(model)
		print(f'Passos válidos: \33[35m{vetor}\33[m')
		if conjuntoVertices:
			print(f'Esse são os conjuntos de vértices usados (fora de ordem): \33[36m{caminhosUsados(model)}\33[m')
		if ordemVertices:
			print(f"Ordem de passagem pelos vértices: \33[33m{ordemValida(passo,model)}\33[m")
	print()


def valoresValidos(model):
	if model:
		return list(filter(lambda x: x>0, model ))


def calcularPosicao(passos):
	pos=[]
	for item in passos:
		pos.append(int(ceil(item/numPassos))-1)
	return pos


def retornarIdxVertices(model):
	if model:
		a=list(filter(lambda x: x>0, model ))
		return calcularPosicao(a)


def caminhosUsados(model):
	pos=retornarIdxVertices(model)
	vet=[]
	for item in pos:
		vet.append(arestas[item])
	return vet


def ordemValida(passo, model):
	valores = valoresValidos(model)
	vertices = caminhosUsados(model)
	#entrada -> arestas
	arestas = lerArq()
	pos = int(passo /numPassos)
	saida = []
	for valido in range(0,len(valores)):
		if passo == valores[valido]:
			aux = arestas[pos]
			saida.append(aux[0])
			vertices.remove(aux)
	while vertices != []:
		for item in vertices:
			if item[0] == aux[1]:
				aux = item
				saida.append(aux[0])
				if len(vertices) == 1:
					saida.append(aux[1])
				vertices.remove(aux)
				break
	return saida
