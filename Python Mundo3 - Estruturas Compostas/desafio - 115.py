def inserirArquivo(nome, idade):
    arquivo = open('pessoas.txt', 'a')
    arquivo.write(addPessoas(nome, idade))


def addPessoas(nome, idade):
    return f'{nome},{idade}\n'


def titulo():
    return 'PESSOAS CADASTRADAS'.center(50)


def verArquivo():

    print('\033[0;30m-'*50)
    print(titulo())
    print('-'*50)

    arquivo = open('pessoas.txt', 'r')
    for linha in arquivo:
        conteudo = linha.replace('\n', '').split(',')
        print(f'{conteudo[0]:<40}', end='')
        print(f' {conteudo[1]} anos', end='')
        print()

    arquivo.close()


def isInt(valor):  # or: isinstance(y, float)-> retorna True ou False
    try:
        int(valor)
    except ValueError:
        return False
    except KeyboardInterrupt:
        return False
    return True


def menu():
    while True:
        print('\033[0;30m-'*50)
        print('MENU PRINCIPAL'.center(50))
        print('-' * 50)
        print('\033[m\033[0;33m1 -\033[m \033[0;34mVer pessoas cadastradas\n', end='\033[m')
        print('\033[0;33m2 -\033[m \033[0;34mCadastrar nova pessoa\n', end='\033[m')
        print('\033[0;33m3 -\033[m \033[0;34mSair do sistema\n', end='\033[m')

        opcao = str(input('\033[0;32mSua opção: \033[m'))
        # print('\033[0;31mO usuário resolveu não realizar nenhuma operação! \033[m')

        if opcao == '1':
            verArquivo()
        elif opcao == '2':
            nome = str(input('\033[0;32mDigite seu nome: \033[m'))
            idade = str(input('\033[0;32mIdade: \033[m')).strip()
            while True:
                if isInt(idade):
                    break
                else:
                    idade = str(input('\033[0;31mErro. Digite um número inteiro válido!: \033[m'))
            inserirArquivo(nome, idade)
        elif opcao == '3':
            print('\033[0;30mObrigado pela visita! Volte sempre!\033[m')
            break


# Programa Principal
menu()




