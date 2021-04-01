# Clinica

## Objetivos

1. Exercitar a modelagem de um domínio a partir de uma situação real;
2. Desenvolver atividades de projeto de banco de dados;
3. Construir um banco de dados usando a linguagem SQL;
4. Implementar uma aplicação que acesse ao banco de dados criado.

Foi utilizado o PostgreSQL para a criação banco de dados.

## Etapas

Etapa | Título | Descrição
:---------:|----------|---------
 1 | Definição do domínio do sistema | Descreva, em um documento, o domínio usado como base para o banco de dados/sistema.
 2 | Descrição de Requisitos | Descreva, em um documento, um domínio a ser modelado e implementado em um sistema, explicando, resumidamente, os requisitos do sistema com suas entidades principais.
 3 | Modelagem do diagrama ER | Crie um Diagrama Entidade-Relacionamento contendo os seguintes elementos: um mínimo de cinco entidades, no mínimo dois atributos por entidade, especialização/generalização, atributo(s) multivalorado(s), atributo(s) composto(s), relacionamento(s) com atributo(s) e entidade(s) fraca(s).
 4 | Mapeamento do Modelo Relacional | Mapear o DER do item 3 para um Modelo Relacional que deve ser representado através de uma notação textual.
 5 | SGBD | Implementar os seguintes itens em um SGBD referentes ao Modelo Relacional criado na etapa 4:  criar o esquema do banco, povoar o banco com dados (pelo menos 10 tuplas em cada relação) e criar consultas (pelo menos 5) e visões (pelo menos uma) realmente útil para o sistema.
 6 | Função, gatilho e usuários | Implementar os itens a seguir em SGBD: criar um procedimento armazenado (Stored Procedure), criar um gatilho (Trigger) não relacionado ao Stored Procudure anterior e criar dois usuários do banco de dados,um deve ter acesso administrativo e o outro deve ter acesso somente de leitura para o banco de dados criado.
 7 | Aplicação | Implementar uma aplicação simples que faz consultas, inserções, atualizações e remoções em relações criadas no trabalho. As consultas aos dados devem ser baseadas nas consultas/visões/procedimentos armazenados criados nas etapas 5 e 6.
