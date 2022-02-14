.data
	f0: .asciiz "Compra negada, bit da pulseira incorreto."
	f1: .asciiz "Compra negada, valor acima do limite permitido."
	f2: .asciiz "\nCompra efetuada com sucesso."
	f3: .asciiz "Digite o valor a ser pago: "
	f4: .asciiz "\nDigite a sua senha: "
	f5: .asciiz "Digite o numero do cartão: "
	f6: .asciiz "Digite o bit da pulseira: "
	f7: .asciiz "\nO valor pago foi: "
	f8: .asciiz "\nO numero do cartão é:"
	f9: .asciiz "Lembre se sua senha não pode comecar com zero.\n"
		    "Senha incorreta, digite novamente sua senha:"
	f10:
	ncartao: .space 17
	zero: .float 0.0
	mil: .float 1001
	
.text

.macro sucesso
	li $v0,31
	li $a0,62 	#Tom
	li $a1,200 	#Duração
	li $a3,100 	#Volume
	syscall

	li $v0,31
	li $a0,55 	#Tom
	li $a1,200 	#Duração
	li $a3,100 	#Volume
	syscall

	li $v0,31
	li $a0,62 	#Tom
	li $a1,200	#Duração
	li $a3,100 	#Volume
	syscall

	li $v0,31
	li $a0,55 	#Tom
	li $a1,200 	#Duração
	li $a3,100 	#Volume
	syscall
.end_macro 

.macro negado
	li $v0,31
	li $a0,52 	#Tom
	li $a1,200 	#Duração
	li $a3,100 	#Volume
	syscall

	li $v0,31
	li $a0,45 	#Tom
	li $a1,200 	#Duração
	li $a3,100 	#Volume
	syscall

	li $v0,31
	li $a0,52 	#Tom
	li $a1,200	#Duração
	li $a3,100 	#Volume
	syscall

	li $v0,31
	li $a0,45 	#Tom
	li $a1,200	#Duração
	li $a3,100 	#Volume
	syscall
.end_macro

.macro Cartao(%string%,%reg%,%limite%) 

Inicio:
	li $v0, 4 		#Chama a função de imprimir
	la $a0, f8		#Carrega a frase "Digite o numero do cartão:"
	syscall			#Executa e imprime a frase
	
	li $v0, 8   		# Pega a entrada
    	la $a0, %string%  	
    	li $a1, %limite%	# Limita a entrada a 16 bits
    	move %reg%, $a0   	# Salva a string digitada em $t5
    	syscall
    	li $t7,1
    	
Laço:				#Verifica se o que está na string é um numero
	lb $a0, (%reg%)		
	beq $a0, 0, Fim		#Verifica se o valor em a0 é igual a zero (NULL), se for vai para o fim
	blt $a0, 48, Inicio	#Verifica se o valor em a0 é menor do 48 na tabela ASCII, se for ele pede de novo o cartão
	bgt $a0, 57, Inicio	#Verifica se o valor em a0 é maior do 57 na tabela ASCII, se for ele pede de novo o cartaõ
	add $t7, $t7, 1		#Acrecenta 1 em t7
	add %reg%, %reg%, 1	#Soma 1 no registrador passado
	j Laço			#Se não entra em nenhuma das condições acima, ele passa para o próximo item na string
	
Fim:
	blt $t7, %limite%, Inicio	#Se for	nulo ele pede novamente o cartão
.end_macro 
   

main:
	li $v0, 4 		#Chama a função para imprimir
	la $a0, f6		#Carrega a frase "Digite o bit da pulseira:"
	syscall			#Pede o bit da pulseira
	
	li $v0, 5 		#Pega do teclado o valor
	syscall			#Executa
	move $t0, $v0		#Recebe o bit da pulseira
	
	li $t9, 0		#Armazena 1 em t9
	beq $t0, $t9, Valor	#Verifica se o bit é igual a valor em t9
	j Negada		#Se não for nega a compra

Valor:		
	li $v0, 4 		#Chama a função para imprimir
	la $a0, f3		#Carrega a frase "Digite o valor a ser pago:"
	syscall			#Executa e imprime a frase
	
	li $v0, 6 		#Pega o valor digitado pelo usuário
	syscall			#Executa e armazena o valor digitado em f0		
	
	lwc1 $f4, mil		#Salva 1000 em f4
	c.lt.s $f0,$f4 		#Verfica se o valor de f0 é menor do que o mil
	bc1t Pagamento		#Se for ele vai para "Pagamento"
	bc1f NegadoValor	#Se não for ele vai para "Negado Valor"
	
Pagamento:	
	 	
    	Cartao(ncartao,$t4,17)

    	li $v0, 4 		#Chama a função de imprimir
	la $a0, f4		#Carrega a frase "Digite a senha do cartão:"
	syscall			#Executa e imprime a frase
	
	li $v0, 5 		#Pega valor digitado pelo usuario
	syscall			#Executa
	move $t3, $v0		#Recebe a senha do cartão em t3
	
	li $t9, 1000		#Armazena 1 em t9
	bge $t3, $t9, Confirmada	#Verifica se o bit é maior do 1000
	j Senha			#Se a senha comecar com 0 ou for menor que 1000, pede novamente a senha

Senha:
	
	li $v0, 4 		#Chama a função de imprimir
	la $a0, f9		#Carrega a frase "Lembre se sua senha não pode comecar com zero\n" e "Senha incorreta, digite novamente sua senha:"
	syscall			#Executa e imprime a frase
	
	li $v0, 4 		#Chama a função de imprimir
	la $a0, f4		#Carrega a frase "Digite a senha do cartão:"
	syscall			#Executa e imprime a frase
	
	li $v0, 5 		#Pega valor digitado pelo usuario
	syscall			#Executa
	move $t3, $v0		#Recebe a senha do cartão em t3
	
	li $t9, 1000		#Armazena 1 em t9
	bge $t3, $t9, Confirmada	#Verifica se o bit é maior do que 1000, se for vai para Confirmada
	j Senha			#Se não ele volta para pedir a senha novamente
				
Confirmada:

	sucesso			#Executa o código sonoro de compra com sucesso

	li $v0, 4 		#Chama a função de imprimir
	la $a0, f7		#Carrega a frase "O valor pago foi:"
	syscall			#Executa e imprime a frase
	
	lwc1 $f1,zero		#Carrega em f1 o valor especificado em zero
	
	li $v0, 2		#Chama a função de imprimir inteiros
	add.s $f12,$f0, $f1	#Carrega o valor da compra
	syscall			#Executa e imprime o valor pago
	
	li $v0, 4 		#Chama a função de imprimir
	la $a0, f8		#Carrega a frase "O numero do cartão é:"
	syscall			#Executa e imprime a frase
	
	la $a0, ncartao 	#Carrega o que está salvo no cartao
	li $v0, 4  		
    	syscall			#Executa e imprime a string   
	
	li $v0, 4 		#Chama a função de imprimir
	la $a0, f2		#Imprime a frase "Compra efetuada com sucesso"
	syscall			#Executa e imprime a frase
	
	li $v0, 10		# Código para encerrar o programa
	syscall			# Executa a chamada do SO para encerrar

Negada:

	negado			#Executa o código sonoro de compra negada
	
	li $v0, 4 		#Chama a função de imprimir
	la $a0, f0		#Imprime a frase 0
	syscall	
	
	li $v0, 10		# Código para encerrar o programa
	syscall			# Executa a chamada do SO para encerrar
			
NegadoValor:

	negado			#Executa o código sonoro de compra negada
	
	li $v0, 4 		#Chama a função de imprimir
	la $a0, f1		#Imprime a frase 1
	syscall	
	
	li $v0, 10		# Código para encerrar o programa
	syscall			# Executa a chamada do SO para encerrar
