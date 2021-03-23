# MIPS

## Objetivo

Desenvolver um programa em assembly do MIPS que simule a comunicação de uma payband com uma máquina de pagamento, similar as máquinas depagamento de cartão de crédito.  
A payband (pulseira de pagamento) a ser simulada é um dispositivo que permite pagar compras apenas aproximando-a da máquina de pagamento, eliminando o uso de senhas.

## Requisitos

1. Verificar se o bit de biomatria está ativado(0), se não a compra deve ser negada.
2. Solicitar ao usário o valor a ser pago. Se o valor for superior a 1000 reais a compra deve ser negada.
3. É solicitado a leitura do cartão. Será necessario digitar os 16 números do cartão.
4. Logo em seguida é solicitada a senha do usuário de 4 dígitos
5. Fornecer uma visualização no final do programa com:
   * O número do cartão.
   * O valor da compra.
   * E a frase "Compra efetuada com sucesso!."
