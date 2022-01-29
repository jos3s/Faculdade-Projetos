# Algoritmos de Ordenação e Tabela Hash

- [Algoritmos de Ordenação e Tabela Hash](#algoritmos-de-ordenação-e-tabela-hash)
	- [Parte 1: Algoritmos de Ordenação](#parte-1-algoritmos-de-ordenação)
		- [Relatório](#relatório)
	- [Parte 2: Tabela Hash](#parte-2-tabela-hash)
		- [Relatório](#relatório-1)

## Parte 1: Algoritmos de Ordenação

- Heap Máximo, implementar as funções a seguir: subir, descer, inserir, remover e construir.
- HeapImplementar o HeapSort.
- Implementar o InsertionSort.

### Relatório

Gera relatório com os algoritmos de ordenação implementados. Seguindo essas especificações:

- Gerar aleatoriamente vetores com os tamanhos: 1.000, 100.000, 10.000.000 e 1.000.000.000.
- Construir o gráfico de tempo de execução do HeapSort e do InsertionSort para cada um dos tamanhos citados acima.
Tendo o cuidado de garantir que o mesmo vetor de 1.000 elementos é usado para ambos os algoritmos e isso também deve ser observado para os outros tamanhos: 100.000, 10.000.000 e 1.000.000.000.

## Parte 2: Tabela Hash

Implementar as funções de dispersão (funções hash) considerando os métodos:

- Método da divisão. Considere que a função recebe dois parâmetros (o valor da chave e o tamanho da tabela)
- Método da dobra
  - considere que as chaves são números decimais e que o tamanho da tabela é uma potência de 10 (isto é, 10, 100, 1000, 10000,...). Faça uma função de dispersão para operação ’+’ (lembre-se de
não considerar o vai 1).
- Método da multiplicação. Considere que as chaves são números decimais e que o tamanho da tabela é uma potência de 10 (isto é, 10, 100, 1000, 10000,...)
- Método da análise de dígitos
  - considere que as n chaves são números decimais, que o tamanho da tabela é uma potência de 10 (isto é, 10, 100, 1000, 10000,...) e que a função recebe 4 parâmetros: o valor da chave, o número de dígitos que serão escolhidos da chave, um vetor com todas as chaves para calcular a distribuição e o tamanho do vetor das chaves.
  - faça uma função de dispersão para cada um dos desvios de distribuição

### Relatório

Gera relatório com os algoritmos de ordenação implementados. Seguindo essas especificações:

- Crie 5 tabelas (vetores) de tamanho 100.000:
  - 1 tabela para o Método da dobra
  - 1 tabela para o Método da divisão
  - 1 tabela para o Método da multiplicação
  - 2 tabelas para o Método da análise de dígitos (uma tabela para cada desvios de distribuição)
- Crie um vetor de tamanho n para armazenar as chaves que deverão ser escolhidas randomicamente entre 0 e 2.000.000.000.
- Depois percorra o vetor das n chaves inserindo cada chave em cada uma das 5 tabelas utilizando o método específico de cada tabela (divisão, dobra,...). Isto é, em cada uma das 5 cinco tabelas deverão ser inseridas (quando não tiver colisão) as n chaves.

O processo do relatório descrito acima deverá ser refeito 5 vezes considerando os valores para n:

- n = 200.000
- n = 400.000
- n = 600.000
- n = 800.000
- n = 1.000.000

O relatório deverá apresentar um gráfico (quantidade de chaves n) × (no de colisões) em que é mostrado as 5 curvas (uma curva para cada um das tabelas) com os 5 valores n pedidos acima.

Isto é, pelo gráfico podemos ver quantas colisões em cada um dos 5 métodos de função de dispersão ocorreram para n = 200.000 chaves, para n = 400.000 chaves,...
