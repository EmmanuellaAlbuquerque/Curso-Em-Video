numeroUsuario = 0
while True:
    print('-='*20)
    numeroUsuario = int(input('Digite o número que deseja ver a tabuada: [numeroNegativo p/ sair] '))
    print('-='*20)
    if numeroUsuario < 0:
        print('PROGRAMA ENCERRADO COM SUCESSO!')
        break
    for i in range(0, 11):
        print(f'{numeroUsuario} X {i} = {numeroUsuario*i}')
