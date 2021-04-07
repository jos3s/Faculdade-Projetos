# Cliente e Servidor em GO

- [Cliente e Servidor em GO](#cliente-e-servidor-em-go)
	- [Objetivo](#objetivo)
		- [Servidor](#servidor)
		- [Cliente](#cliente)
		- [Funções do programa](#funções-do-programa)
	- [Como usar](#como-usar)
		- [Como executar](#como-executar)

## Objetivo

Implementar um processo de cliente e servidor em GO utilizando sockets.

### Servidor

- O servidor deve ter uma forma de guardar durante a execução:
  - Todos os clientes que estão cadastrados da forma (ID/Senha)
  - Todos os clientes que estão online
  - Todos os filmes que estão cadastrados

- O servidor deverá abrir e permanecer escutando conexões pelo ip local (127.0.0.1) e porta arbitrária (Escolhida pelo aluno).
- Quando uma conexão for iniciada o servidor deverá responder com a opção de login/cadastrar

### Cliente

- O cliente irá implementar um socket no mesmo ip e porta que o servidor.
- Assim que executado o cliente tentará se conectar ao servidor, verificando possíveis erros de conexão.
- Quando conectado, o cliente poderá enviar mensagens para o servidor (cujo possíveis fluxos de execução estão citados acima).

### Funções do programa

| Função | Descrição | Condição de Saída |
| - | - | - |
| Login/Cadastrar | Exibir a opção do cliente cadastar ou logar no servidor | Fazer o cadastro ou logar com sucesso |
| Exibir um Menu | Exibir o Menu com todas opções abaixo | O cliente selecionar uma das funções abaixo |
| Inverter String | O servidor responderá todas as próximas mensagens do cliente com o inverso da mensagem. | O cliente digitar “SAIR” |
| IMC | O servidor irá esperar uma string contendo a altura e o peso do cliente e responderá com o IMC e seu estado corporal. | Após responder, o servidor voltará ao menu |
| Número Aleatório | O servidor irá receber uma string do usuário com inicio do range e o fim do range e irá responder com um número inteiro entre o intervalo | Após responder, o servidor voltará ao menu |
| Mensagem direta | O servidor irá receber o ID do usuário receptor da mensagem, caso o ID escrito esteja online o servidor iráreceber a mensagem. O servidor então enviará uma mensagem para o cliente com o ID passado. | Após enviar a mensagem, o servidor voltará ao menu |
| Chat | O servidor irá repassar qualquer mensagem mandada nessa opção para todos os clientes que também estejam na opção 5 (ou seja, todos que estejam no chat) exceto o emissor da mensagem. | O cliente digitar “SAIR" |
| Cadastrar filme | O servidor irá receber uma string com os dados sobre um filme (título/descrição/diretor). Se o filme não estiver cadastrado, o servidor irá cadastrá-lo na memória, caso contrário o servidor irá responder uma mensagem de erro. | Após enviar a mensagem o servidor voltará ao menu |
| Filme Aleatório | O servidor irá sortear um filme cadastradr aleatoriamente e irá responder para o cliente. | Após enviar a mensagem, o servidor voltará ao menu |
| Sair | O servidor irá encerrar a conexão desse cliente e removê-lo da lista dos clientes online. | Receber "SAIR" do cliente |

O servidor deverá aceitar e tratar múltiplos clientes concorrentemente.O servidor e o cliente devem ser implementados na linguagem Go

- O tipo de socket usado será UDP.
- O prazo máximo para apresentação do trabalho ao professor é o fim do semestre letivo.

## Como usar

Para rodar o código é necessário ter a pasta *sck* dentro da pasta de *src* do GO (`~/GO/src`). O caminho da localização da pasta GO depende do sistema operacional usado para rodar o código.

### Como executar

Para executar o programa é recomendado usar duas ou três instâncias do terminal, uma para o servidor e os outras para a execução do cliente. O códigos podem ser rodados usando:

```bash
go run servidor.go
```

E logo após:

```bash
go run cliente/cliente.go
```
