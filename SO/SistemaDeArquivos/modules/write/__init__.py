import math


def writeFile(tabDiretorio: [[str, int]], fat: [int], blocks: int, tamBlock: int, disco: [str]):
  """Função que escreve o conteudo do arquivo no disco e na tabela fat

  Args:
      tabDiretorio: array de diretorios 
      fat: array que armazena o dados da tabela fat
      blocks: número de blocos do disco
      tamBlock: tamanho do bloco do disco
      disco: array que representa o disco de dados
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


def writeFAT(fat: [int], blocks: int, tamBlock: int, write: [str], tituloArquivo: str, tabDiretorio: [[str, int]]):
  """Escreva no array fat o uso de disco pelo arquivo

  Args:
      fat: array que armazena o dados da tabela fat
      blocks: número de blocos do disco
      tamBlock: tamanho do bloco do disco
      write: conteudo a ser escrito no disco
      tituloArquivo titulo do arquivo que está recebendo os dados
      tabDiretorio: array de diretorios 
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
        #verifico se a posição da tabela fat não está alocada e se o arquivo ainda não está no disco
        block = i
        #defino como bloco inicial o indicie atual da tabela fat e removo um do número de blocos que o arquivo vai usar
        contBlocks -= 1
      elif fat[i] == None and block != -1 and contBlocks > 0:
        #se posição da tabela fat não está alocada, se ainda preciso de bloco no disco e se existe um bloco anterior já definido
        #defino a usando o bloco como indice da tabela que vai indicar o bloco atual livre
        fat[block] = i
        #defino o novo bloco anterior como o indice atual
        block = i
        contBlocks -= 1
      if fat[i] == None and block != -1 and contBlocks <= 0:
        #se o posição da tabela fat não está alocada, se o bloco anterior já foi definido e se não existe mais blocos a serem alocados defino o bloco atual como fim do arquivo
        fat[block] = -1
        break


def writeDisco(write: str, tituloArquivo: str, fat: [int], tamBlock: int, disco: [str], tabDiretorio: [[str, int]]):
  """Escreve no disco dados do arquivo

  Args:
      write: conteudo a ser escrito no disco
      tituloArquivo: titulo do arquivo que está recebendo os dados
      fat: array que armazena o dados da tabela fat
      tamBlock: tamanho do bloco do disco
      disco: array que representa o disco de dados
      tabDiretorio: array de diretorios 
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
      #se o valor na tabela fat for igual ao seu index ou -1 signfica que chegue ao fim das posições alocadas na tabela fat
      break

  for item in pos:
    #cada item em pos, representa um bloco do disco
    tam = tamBlock
    for i in range(len(write)):
      #faço um loop para cada caractere que preciso escrever
      if tam > 0:
        #escrevendo o caractere no disco apenas até preencher um bloco do disco
        disco[(item*tamBlock)+i] = write[i]
        tam -= 1
    #removo da frase original a quantidade de caracteres que escrevi no disco
    write = write[tamBlock:]
    #repito isso até escrever no ultimo bloco alocado
