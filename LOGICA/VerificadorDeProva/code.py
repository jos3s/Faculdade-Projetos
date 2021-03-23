import funcoes

if __name__ == "__main__":
    try:
        valido=funcoes.validarEntrada()
        if valido:
            print("O formato do dados de entrada é valido.\n")
            axiomas=funcoes.lerArq()
            valido=True
            for axioma in axiomas:
                valido=funcoes.validarFormula(axioma[1])
                if not valido:
                    print(f'A fórmula da linha {axioma[0]} é inválida.')
                    break
                if "MP" in axioma[2]:
                    valido=funcoes.compararMP(axioma,axiomas)
                    if not valido: break
                else:
                    valido=funcoes.compararAxiomas(axioma)
                    if not valido: break
            if valido:
                print("\nEssa verificação é válida, ou seja, a prova é válida.")
        if not valido:
            print("\nEssa verificação é inválida, ou seja, a prova é inválida.")
    except:
        print("Ocorreu um erro na validação da entrada, verifique o arquivo 'entrada.txt'.")
        pass