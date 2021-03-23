from copy import deepcopy

def lerArq():
    try:
        a = open("entrada.txt", 'rt',encoding="utf8")
    except:
        print('Erro na leitura do arquivo')
    else:
        linhas=[]
        for linha in a:
            if linha.find("#")==0:
                continue
            else:
                nLinha=linha.rstrip('\n').strip(' ').split(' ')
                formatAxioma(nLinha)
                if not isParentesesExternos(nLinha[1], 1, 1):
                    nLinha[1] = '({0})'.format(nLinha[1])
                linhas.append(nLinha)
        a.close()
        return linhas
    # retorna uma lista com listas dentro que contem os itens do 
    # arquivo (axioma, qual axioma ou MPx,x e as subistituições se existirem)


def formatAxioma(linha):
    while (linha[2] == '') or (linha[2][0] != 'A') and (linha[2][0] != 'M'):
        if linha[2] != '':
            linha[1] += linha[2]
        del(linha[2])


def isParentesesExternos(axioma, num, ac):
    if axioma[0] == '(' and axioma[len(axioma)-1] == ')':
        if axioma[num] == ')' and ac == 1 and num == len(axioma)-1:
            return True
        elif axioma[num] == ')' and num == len(axioma)-1:
            return False
        elif axioma[num] == ')' and ac == 1:
            return False
        elif axioma[num] == ')':
            return isParentesesExternos(axioma, num+1, ac-1)
        if axioma[num] == '(':
            return isParentesesExternos(axioma, num+1, ac+1)
        return isParentesesExternos(axioma, num+1, ac)


def defAxiomas():
    axiomas=[]
    a1=('p>(q>p)','p','q')
    a2=('(p>(q>r))>((p>q)>(p>r))','p','q','r')
    a3=('p>(q>(p&q))','p','q')
    a4=('(p&q)>p','p','q')
    a5=('(p&q)>q','p','q')
    a6=('p>(pVq)','p','q')
    a7=('q>(pVq)','p','q')
    a8=('(p>r)>((q>r)>((p&q)>r))','p','q','r')
    a9=('(p>q)>((p>¬q)>¬p)','p','q')
    a10=('¬¬p>p','p')
    axiomas=[a1,a2,a3,a4,a5,a6,a7,a8,a9,a10]
    return axiomas


def validarEntrada():
    if validarNumeracao():
        linhas=lerArq()
        axis=defAxiomas()
        cont=1
        for n in range(0,len(linhas)):
            tam=len(linhas[n])
            linha=linhas[n]
            if tam==3:
                modosPoneis=str(linha[2])
                if not validarEntradaMP(cont,modosPoneis):
                    return False
            elif tam>3 and tam<7:
                axioPraSubist=linha[2].strip('A')
                if len(axioPraSubist)!=1 and axioPraSubist!="10":
                    print(f"A linha {cont} tem o axioma base inválido.")
                    return False
                if not(validarEntradaAxioma(tam,linha,axis)):
                    print(f'A linha {cont} não possui os átomos esperados para a subistituição.')
                    return False
            else:      
                print(f'A linha "{linha}" não corresponde ao formato esperado')
                return False
            cont+=1
        return True
    print('A númeração das linhas é inválida')
    return False


def validarNumeracao():
    linhas=lerArq()
    nDaLinha=[]
    for linha in linhas:
        nDaLinha.append(int(linha[0]))
    
    cont=1
    for num in nDaLinha:
        if num!=cont:
            return False
        else:
            cont+=1
    
    return True


def validarEntradaMP(cont, modosPoneis):
    if not modosPoneis.find("MP"):
        modosPoneis=modosPoneis.strip("MP")
        if len(modosPoneis)!=3 or not modosPoneis.find(","):
            print(f'O MP da linha {cont} é inválido.')
            return False
        numLinhas=modosPoneis.split(",")
        if not int(numLinhas[0])<cont or not int(numLinhas[1])<cont:
            print(f'A linha {cont} faz Modus Ponens com linhas inválidas.')
            return False
    else:
        print(f'A linha {cont} é inválida.')
        return False
    return True


def validarEntradaAxioma(tam,linha,axis):
    itensPraSubist=tam-3
    axioPraSubist=linha[2].strip('A')
    axioASerSubist=axis[int(axioPraSubist)-1]
    ##print(axioASerSubist)
    itemsSubistituiveis=len(axioASerSubist)-1
    #print(f'{itemsSubistituiveis} {itensPraSubist}')
    if itemsSubistituiveis!=itensPraSubist:
        return False
    
    atomos=axioASerSubist[1:]
    n=0
    subistitucao=linha[3:]
    #print(f'{atomos} {subistitucao}')
    for item in subistitucao:
        novosAtomos=str(deepcopy(item))
        atomo=novosAtomos.split('=')
        #print(atomo)
        if atomo[0]==atomos[n]:
            n+=1
        else:
            return False 
    return True
  

def validarLiteral(ant, lit, prox):
    if ord(lit) >= 97 and ord(lit) <= 122:
        if ord(ant) >= 97 and ord(ant) <= 122 or ant == ')':
            return False
        if ord(prox) >= 97 and ord(prox) <= 122:
            return False
        elif prox == '(' or prox == '¬':
            return False
    elif lit == '¬':
        if ord(ant) >= 97 and ord(ant) <= 122 or ant == ')':
            return False
        if prox == '>' or prox == 'V' or prox == '&' or prox == ')' or prox == chr(0):
            return False
    elif lit == 'V' or lit == '&' or lit == '>':
        if ant == '¬' or ant == '(' or ant == '>' or ant == '&' or ant == 'V' or ant == chr(0):
            return False
        if prox == '&' or prox == '>' or prox == ')' or prox == 'V' or prox == chr(0):
            return False
    elif lit == '(':
        if ord(ant) >= 97 and ord(ant) <= 122 or ant == ')':
            return False
        if prox == ')' or prox == '>' or prox == 'V' or prox == '&' or prox == chr(0):
            return False
    elif lit == ')':
        if ant == '(' or ant == '>' or ant == 'V' or ant == '&' or ant == '¬' or ant == chr(0):
            return False
        if ord(prox) >= 97 and ord(prox) <= 122 or prox == '(' or prox == '¬':
            return False
    return True

   
def validarFormula(form):
    i = 0
    while i < len(form):
        if len(form) == 1:
            if ord(form[i]) < 97 or ord(form[i]) > 122:
                return False
        elif i == 0:
            if not(validarLiteral(chr(0), form[i], form[i + 1])):
                return False
        elif i == len(form) - 1:
            if not(validarLiteral(form[i - 1], form[i], chr(0))):
                return False
        else:
            if not(validarLiteral(form[i - 1], form[i], form[i + 1])):
                return False
        i = i + 1
    return True


def compararAxiomas(axioma):
    if axioma[1]==subistituirAxioma(axioma):
        print(f"Formula da linha {axioma[0]} é válida")
    else:
        print(f"Formula da linha {axioma[0]} é inválida")
        return False
    return True


def subistituirAxioma(axioma):
    axiomas=defAxiomas()
    numAx=int(axioma[2].strip('A'))
    axiomaBase=axiomas[numAx-1][0]
    atomosNovos=devolverAtomos(axioma[3:])
    arryAxio=list(axiomaBase)
    for n in range(len(arryAxio)):
        if arryAxio[n]=="p":
            arryAxio[n]=atomosNovos[0][1]
        elif arryAxio[n]=="q":
            arryAxio[n]=atomosNovos[1][1]
        elif arryAxio[n]=="r":
            arryAxio[n]=atomosNovos[2][1]
    
    resultadoFinal=['(']
    resultadoFinal.extend(arryAxio)
    resultadoFinal.append(")")
    return "".join(resultadoFinal)


def devolverAtomos(atomos):
    lista=[]
    for item in atomos:
        lista.append(item.split("="))
    return lista


def compararMP(axioma,axiomas):
    if axioma[1]==montarMP(axioma,axiomas):
        print(f"MP da linha {axioma[0]} é válido")
    else:
        print(f"MP da linha {axioma[0]} é inválido")
        return False
    return True


def montarMP(axioma, axiomas):
    nLinhas=axioma[2].strip("MP").split(",")
    l1=str(axiomas[int(nLinhas[0])-1][1])
    l2=str(axiomas[int(nLinhas[1])-1][1])
    res=""
    if len(l1)>len(l2):
        if l1.find(l2):
            res=l1.replace(l2,'')
    elif l2.find(l1):
        res=l2.replace(l1,'')
    res=res[2:-1]
    return res