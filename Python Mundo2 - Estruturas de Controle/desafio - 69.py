# Análise de Dados
contadorIdade = contadorHomens = contadorMulheres = 0
while True:
    print('-='*20)
    print(' ANÁLISE DE DADOS| CADASTRE UMA PESSOA')
    print('-=' * 20)
    idade = int(input('Digite a idade: '))
    sexo = str(input('Digite o sexo: [F/M] ')).strip().upper()
    while sexo not in 'FM':
        sexo = str(input('Digite o sexo: [F/M] ')).strip().upper()
    if idade > 18:
        contadorIdade += 1
    if sexo == 'M':
        contadorHomens += 1
    if sexo == 'F' and idade < 20:
        contadorMulheres += 1
    desejaContinuar = str(input('Digite s p/ continuar e n p/ parar\: ')).strip().upper()
    while desejaContinuar not in 'SN':
        desejaContinuar = str(input('Digite s p/ continuar e n p/ parar\: ')).strip().upper()
    if desejaContinuar == 'N':
        print('PROGRAMA ENCERRADO COM SUCESSO!')
        break
print(f'''{contadorIdade} pessoas tem MAIS de 18 anos
{contadorHomens} HOMENS foram cadastrados
{contadorMulheres} MULHERES tem MENOS de 20 anos.''')
