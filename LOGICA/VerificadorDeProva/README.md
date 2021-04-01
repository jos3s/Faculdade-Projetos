# Verificador de Prova do Método Axiomatico

- [Verificador de Prova do Método Axiomatico](#verificador-de-prova-do-método-axiomatico)
  - [Equipe](#equipe)
  - [Objetivo](#objetivo)
  - [Como funciona um verificador de prova?](#como-funciona-um-verificador-de-prova)
    - [As fórmulas usadas deverão ter o seguinte alfabeto:](#as-fórmulas-usadas-deverão-ter-o-seguinte-alfabeto)
    - [As regras de formação das fórmulas seguem as propostas em sala de aula:](#as-regras-de-formação-das-fórmulas-seguem-as-propostas-em-sala-de-aula)
    - [Exemplo de provas](#exemplo-de-provas)
  - [Como Usar](#como-usar)

## Equipe

- [José Ulisses](https://github.com/jos3s)
- [Jeferson Ribeiro Reges](https://github.com/JeffEngMaster)
- [Luis Gustavo Girão Cardial](https://github.com/Mufado)

## Objetivo

Construir um verificador de prova para o método axiomático.

## Como funciona um verificador de prova?

Dada uma prova no sistema axiomático, ele verifica se a prova proposta está construída de forma correta, ou seja, se todas as instâncias de axiomas e uso do modus ponens foram usados de forma correta.

### As fórmulas usadas deverão ter o seguinte alfabeto:

1. símbolos atômicos: a,b,c,....,w,y,x,z. (letras do alfabeto em minúsculo);
2. conectivos binários: & (conjunção), v (disjunção), > (implicação);
3. conectivo unário: ¬ (negação);
4. símbolos auxiliares: ),( - parênteses

### As regras de formação das fórmulas seguem as propostas em sala de aula:

1. Todas as proposições atômicas são fórmulas;
2. Se A e B são fórmulas então (A&B), (AvB), (A>B) também são fórmulas;
3. Se A é fórmula então (¬A) também é fórmula;
4. Toda fórmula só pode ser obtida por 1,2 e 3.

### Exemplo de provas

**Prova Correta:**  
1 (a>((a>a)>a)) A1 p=a;q=(a>a)  
2 ((a>((a>a)>a)) > ((a>(a>a))>(a>a))) A2 p=a;q=a;r=a  
3 ((a>(a>a))>(a>a)) MP 1,2  
4 (a>(a>a)) A1 p=a;q=a  
5 (a>a) MP 3,4  

A prova acima está correta pois todas as instâncias de axiomas foram utilizadas de forma correta, assim como o modus ponens.

**Prova Incorreta:**  
1 (a>((a>a)>a)) A1 p=a;q=(a>a)  
2 ((a>((a>a)>a)) > ((a>(a>a))>(a>a))) A2 p=a;q=a;r=a  
5 ((a>(a>a))>(a>a)) MP 1,2  
6 (a>(a>a)) A1 p=a;q=a  
7 (a>a) MP 5,6  

A prova acima está errada pois a numeração não está correta (as linhas 3 e 4 foram suprimidas).

## Como Usar

Será necessário alterar as informações contidas no arquivo **entrada.txt** seguindo o padrão de 'numerolinha axioma numeroAxioma subisituições' ou 'numerolinha axioma ModusPoneis' (exemplo: '1 (a>((a>a)>a)) A1 p=a;q=(a>a)'), sendo que cada linha do arquivo só pode conter axioma ou *modus ponens*.

Após isso deve executar o comando `python code.py` no terminal, para ver o resultado do programa.
