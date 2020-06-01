# Aprovador de empréstimo bancário
valorDaCasa = float(input('Digite o valor da casa: '))
salario = float(input('Digite seu salário: '))
pagamentoPAnos = int(input('Digite daqui a quantos anos irá pagar: '))

prestacaoMensal = valorDaCasa/(pagamentoPAnos*12)
print('A prestação será {:.2f} por mês!'.format(prestacaoMensal))

# Prestação não pode exceder 30% do salario
if prestacaoMensal > (0.3*salario):
    print('Empréstimo negado! Excedeu o limite estimado.')
else:
    print('Empréstimo Concedido!')