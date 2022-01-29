# AVL

- [AVL](#avl)
	- [Implementações](#implementações)
	- [Testes](#testes)
	- [Apresentação](#apresentação)

## Implementações

1. Implementar as funções inserir e remover para AVL. Essas implementações devem seguir os algoritmos vistos em aula.
2. Implementar uma função que verifica se uma árvore é AVL fazendo o cálculo das alturas das subárvores de cada nó e verificando se o campo ’bal’ de cada nó está realmente correto.
3. Implementar uma função que conta a quantidades de nós de uma AVL.

## Testes

1. Deve-se criar 1.000 AVL’s
2. Em cada AVL deve-se inserir aleatoriamente 10.000 nós onde a chave de cada nó está entre 0 e 100.000 (verificar se a AVL possui os 10.000 pelo algoritmo de contagem de nós)
3. Após todas as inserções verificar se a árvore é AVL pelo algoritmo de verifica ̧cão.
4. Remover 1.000 nós (verificar se a AVL possui os 9.000 nós pelo algoritmo de contagem de nós)
5. Após todas as remoções verificar se a árvore é AVL pelo algoritmo de verifica ̧cão.
O processo anterior pode ser realizado com uma AVL por vez, isto é, não é necessário tem 1.000 AVL’s ao mesmo tempo em sua memória, mas apenas 1 por vez.

## Apresentação

Deverá ser feito um video de no máximo 7 minutos apresentado o trabalho realizado focando nos seguintes tópicos:

- dificuldades encontradas e como foram resolvidas.
- apresentação dos códigos de cada algoritmo pedido com atenção principal no inserir e remover.
- demonstração de funcionamento do programa para uma caso pequeno (inserção de 100 nós e remoção de 10 nós - seguindo os passos de teste acima para uma  única AVL)
