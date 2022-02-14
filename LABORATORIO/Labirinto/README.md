# Labirinto

## Conteudo
  - [Conteudo](#conteudo)
  - [Integrantes:](#integrantes)
  - [Sobre](#sobre)
  - [Instalação e uso](#instalação-e-uso)

## Integrantes:

![#2508D5](https://placehold.it/15/2508D5/000000?text=+) [Jeferson Ribeiro](https://github.com/Woozymandias)

![#0883D5](https://placehold.it/15/0883D5/000000?text=+) Isaac Freitas

![#F6BC0A](https://placehold.it/15/F6BC0A/000000?text=+) José Ulisses

## Sobre 

Gerar dois códigos em C com o objetivo de gerar um labirinto aleatório e um caminho de saída, que vão ser salvos dois arquivos:

1. Criação do Labirinto - Gerar um labirinto com tamanho dinâmico definido pelo usuário, como todas as regiões no mesmo acessiveis.
2. Resolução do Labirinto - Percorrer o labirinto com algunas preferências na sua forma de andar (para baixo, direita, para cima, esquerda) e se ele entrar um beco sem saída ele deve voltar substituindo a ' # ' por uma ' \ '.

## Instalação e uso

### Pré-requisitos

- Code::Blocks qualquer IDE para C (compilar pelo terminal também é possivel)
- Bilbiotecas como a stdlib.h, a stdio.h e a time.h instaladas.

### Uso

- Compilar 'criacaoLabirinto.c'
- Excecutar 'criacaoLabirinto.exe'
- Vai sair um arquivo txt contendo o labirinto gerado
- Compilar 'resolverLabirinto.c'
- Excecutar 'resolverLabirinto.exe'
-  Vai sair um arquivo txt contendo o labirinto resolvido