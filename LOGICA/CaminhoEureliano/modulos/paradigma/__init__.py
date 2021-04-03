from pysat.solvers import Glucose4
from pysat.formula import CNF
from modulos.matriz import criarMatriz, lerArq

def getPdgs(matriz, formula, lin=0, col=0):
	arestas = lerArq()
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
		#print('negarLinhaContrario')
		formula.append([-valor, -matriz[lin][col]])


def resolver(passo):
	formula=CNF()
	g=Glucose4()
	getPdgs(criarMatriz(),formula)
	formula.append([passo])
	g.append_formula(formula)
	print(f'{passo}  {g.solve()}')
	valoresValidos(g.get_model())
	#print(g.get_model())


def valoresValidos(model):
	if model:
		a=[]
		for item in model:
			if item>0:
				a.append(item)
		print(f'{a}')
