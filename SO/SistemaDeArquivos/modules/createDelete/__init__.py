def createFile(tabDiretorio: [[str, int]]):
  """É a função que criar o arquivo na tabela de diretorio

  Args:
      tabDiretorio: array de diretorios 
  """
  print('\n=Criar Arquivo=')
  tituloArquivo = input("Digite o nome do arquivo: ")
  tabDiretorio.append([tituloArquivo, -1])
  print('Arquivo criado\n')


def deleteFile(tabDiretorio: [[str, int]], fat:[int]):
  """É a função que deleta o arquivo na tabela de diretorio e limpa a tabela fat

  Args:
      tabDiretorio: array de diretorios 
      fat: array que armazena o dados da tabela fat
  """
  print('\n=Deletar Arquivo=')
  tituloArquivo = input("Digite o nome do arquivo: ")
  try:
    for i in range(len(tabDiretorio)):
      #para cada item da tabela de diretorios verifica se o titulo digitado existe nessa tabela
      if tabDiretorio[i][0] == tituloArquivo:
        if tabDiretorio[i][1] == -1:
          #se o arquivo existir e não tiver dado no disco o item é excluído do array tabDiretorio
          del tabDiretorio[i]
        else:
          #se tiver dado no disco, pego o primeiro endereço da tabela fat
          pos = [tabDiretorio[i][1]]
          while True:
            #ando pela sequencia de posições alocadas até encontrar o item que tem o -1
            proxPos = fat[pos[-1]]
            if tabDiretorio[i][1] == proxPos or proxPos == -1:
              break
            #com isso tenho um array com todas as posições que um arquivo tem na tabela fat
          for item in pos:
            fat[item] = None
            # passo por todos os itens do array sobreescrevendo os valores
          del tabDiretorio[i]
          #deleto o item da tabela de arquivos do diretorio
        print('Item apagado\n')
        break
  except:
    print('Houve um erro na exclusão do arquivo')
