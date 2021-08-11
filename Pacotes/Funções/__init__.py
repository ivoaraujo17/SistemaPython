

def menu():
    while True:
        print('\nEscolha o que deseja fazer entre as opções abaixo')
        print('\n1 - CRIAR TABELA\n2 - INSERIR DADOS\n3 - LER TABELA')
        while True:
            try:
                op = int(input('\nDigite o número correspondente a sua escolha-> '))
                
                    
            except:
                print('\nOpção invalida, tente novamente!')
            else:
                if op in [1,2,3]:
                    return op
                    break
                print('\nOpção invalida, tente novamente!')