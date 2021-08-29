import math


def writeFile(tabDiretorio, fat, blocks, tamBlock, disco):
  """Função que escreve o conteudo do arquivo no disco e na tabela fat

  Args:
      tabDiretorio ([[string, int]]): array de diretorios 
      fat ([int]): array que armazena o dados da tabela fat
      blocks (int): número de blocos do disco
      tamBlock (int): tamanho do bloco do disco
      disco ([string]): array que representa o disco de dados
  """
  print('\n=Escrever em um Arquivo=')
  tituloArquivo = input("Digite o nome do arquivo: ")
  try:
    for i in range(len(tabDiretorio)):
      #para cada item da tabela de diretorios verifica se o titulo digitado existe nessa tabela
      if tabDiretorio[i][0] == tituloArquivo:
        #se o arquivo existir e pergunto o que usuario deseja escrever
        write = input("Digite o que vai ser salvo: ")
        #Primeiramente escrevo na tabela fat quais blocos o arquivo vai usar no disco
        writeFAT(fat, blocks, tamBlock, list(
            write), tituloArquivo, tabDiretorio)
        #depois escrevo no disco os dados
        writeDisco(write, tituloArquivo, fat, tamBlock, disco, tabDiretorio)
        print('Conteudo salvo\n')
  except:
    print('Houve um error ao salvar no arquivo')


def writeFAT(fat, blocks, tamBlock, write, tituloArquivo, tabDiretorio):
  """Escreva no array fat o uso de disco pelo arquivo

  Args:
      fat ([int]): array que armazena o dados da tabela fat
      blocks (int): número de blocos do disco
      tamBlock (int): tamanho do bloco do disco
      write ([string]): conteudo a ser escrito no disco
      tituloArquivo (string): titulo do arquivo que está recebendo os dados
      tabDiretorio ([[string, int]]): array de diretorios 
  """

  #verifico quantos blocos a frase vai usar
  blocksWrite = math.ceil(len(write) / tamBlock)
  blocksFree = 0
  for item in fat:
    #verifico quantos blocos estão livres no array fat
    if item == None:
      blocksFree += 1

  #se o uso de disco for maior que o total de blocos livres, não é possível escrever
  if blocksFree < blocksWrite:
    print(
        "Nao existe quantidade de blocos disponíveis para salvar o conteudo do arquivo")
  else:
    #representa o valor -1 na tabDiretorio, ou seja, o arquivo não tem dados no disco
    writeTabDirectory = False
    #signfica que o valor do arquivo na tabDiretorio é -1, ou seja, não tem dados
    block = -1
    #salvo quantos blocos o arquivo vai usar no disco
    contBlocks = blocksWrite
    for i in range(len(fat)):
      #laço pelo tamanho da tabela fat
      if fat[i] == None and not writeTabDirectory:
        #se o item for nulo e o arquivo ainda não está na tabela fat, defino na tabDiretorio qual seu bloco inicial
        writeTabDirectory = True
        for j in range(len(tabDiretorio)):
          if tabDiretorio[j][0] == tituloArquivo:
            tabDiretorio[j][1] = i

      if fat[i] == None and block == -1 and contBlocks == 1:
        #se o dados a serem escritos só vão ocupar um bloco, defino que o indice do bloco é o respectivo indice atual da tabela fat
        fat[i] = i
        break
      elif fat[i] == None and block == -1:
        block = i
        contBlocks -= 1
      elif fat[i] == None and block != -1 and contBlocks > 0:
        fat[block] = i
        block = i
        contBlocks -= 1
      if fat[i] == None and block != -1 and contBlocks <= 0:
        fat[block] = -1
        break


def writeDisco(write, tituloArquivo, fat, tamBlock, disco, tabDiretorio):
  """Escreve no disco dados do arquivo

  Args:
      write (string): conteudo a ser escrito no disco
      tituloArquivo (string): titulo do arquivo que está recebendo os dados
      fat ([int]): array que armazena o dados da tabela fat
      tamBlock (int): tamanho do bloco do disco
      disco ([string]): array que representa o disco de dados
      tabDiretorio ([[string, int]]): array de diretorios 
  """
  initialWrite = -1
  for j in range(len(tabDiretorio)):
    #para cada item da tabela de diretorios verifica se o titulo existe nessa tabela
    if tabDiretorio[j][0] == tituloArquivo:
      initialWrite = tabDiretorio[j][1]
      #se o arquivo existir pego o primeiro endereço da tabela fat

  #crior um array que vai armazenar todas as posições da tabela fat do respectivo arquivo
  pos = [initialWrite]
  while True:
    #ando pelos valores de pos (usando sempre o ultimo indice) para encontrar o proximo valor diferente de -1, ou seja, pegando o indice de todos os blocos alocados para o arquivo
    proxPos = fat[pos[-1]]
    if initialWrite == proxPos or proxPos == -1:
      break

  for item in pos:
    #para item em pos, representa um o inicio de um bloco do disco
    tam = tamBlock
    for i in range(len(write)):
      if tam > 0:
        disco[(item*tamBlock)+i] = write[i]
        tam -= 1
    write = write[tamBlock:]
