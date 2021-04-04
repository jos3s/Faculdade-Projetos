from modulos.paradigma import resolver
from modulos.matriz import primeirosPassos, printMatriz,criarMatriz

if __name__ == '__main__':
	while True:
		opc=input("Deseja exibir a matriz de passos?[S/n] ")
		if opc in 'Ss':
			printMatriz(criarMatriz())
			break
		elif opc in 'Nn':
			break
	print("\nExecutando o caminho eureliano: ")
	passo1 = primeirosPassos()
	for item in passo1:
		resolver(item, conjuntoVertices=True,ordemVertices=True)
