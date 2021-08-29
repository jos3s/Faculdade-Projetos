def readFile(tabDiretorio, fat, tamBlock, disco):
  """Funcao que le o arquivo de texto e imprime na tela

  Args:
      tabDiretorio ([[string, int]]): array de diretorios 
      fat ([int]): array que armazena o dados da tabela fat
      tamBlock (int): tamanho do bloco do disco
      disco ([string]): array que representa o disco de dados
  """
  print('\n=Ler Arquivo=')
  tituloArquivo = input("Digite o nome do arquivo: ")
  try:
    for i in range(len(tabDiretorio)):
       #para cada item da tabela de diretorios verifica se o titulo digitado existe nessa tabela
      if tabDiretorio[i][0] == tituloArquivo:
        #se o arquivo existir e tiver dado no disco, pego o primeiro endereço da tabela fat
        pos = [tabDiretorio[i][1]]
        while True:
          proxPos = fat[pos[-1]]
          if tabDiretorio[i][1] == proxPos or proxPos == -1:
            break
          #ando pela sequencia de posições alocadas até encontrar o item que tem o -1
          #com isso tenho um array com todas as posições que um arquivo tem na tabela fat
    read = []
    #read vai ser meu array com as letras que vou ler do disco
    for item in pos:
      #para cada posição da tabela fat
      for i in range(tamBlock):
        #faço um laço pelo tamanho do bloco para ler cada posição correspondente no disco
        # e adicionar ao array read
        read.append(disco[(item*tamBlock)+i])

    #verifico se cada item em read é uma string, pode haver valores None o que daria error
    # e salvo em readStr
    readStr = [i for i in read if isinstance(i, str)]
    #faço uma junção do itens do array readStr e salvo em readJoin
    readJoin = "".join(readStr)
    print('=Conteudo do arquivo=')
    print(f"{readJoin}\n")
  except:
    print('Erro na leitura do arquivo')
