from modules.write import writeFile
from modules.createDelete import createFile, deleteFile
from modules.read import readFile


tabDiretorio = []
opcoesMenu = "Menu: \n1 Criar arquivo \n2 Apagar arquivo  \n3 Escrever no arquivo \n4 Ler arquivo \n5 Inserir ao fim do arquivo (não implementado) \n6 Sair"


if __name__ == "__main__":
  blocks = int(input("Digite o numero de blocos do disco?"))
  tamBlock = int(input("Digite o tamanho do bloco?"))
  print('')
  fat = [None]*blocks
  disco = [None]*(blocks*tamBlock)
  while True:
    print(opcoesMenu)
    opc = int(input('Digite a sua escolha:'))
    if opc == 1:
      createFile(tabDiretorio)
    elif opc == 2:
      deleteFile(tabDiretorio, fat)
    elif opc == 3:
      writeFile(tabDiretorio, fat, blocks, tamBlock, disco)
    elif opc == 4:
      readFile(tabDiretorio, fat, tamBlock, disco)
    elif opc == 5:
      print('Não implementada')
    elif opc == 6:
      print('Programa encerrado')
      break
