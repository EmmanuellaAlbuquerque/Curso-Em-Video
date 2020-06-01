# SIMULADOR BANCO: CAIXA ELETRÔNICO
print('|------'*3)
print(' CAIXA ELETRÔNICO PYTHON ')
print('|------'*3)
valor = int(input('Digite o valor a ser sacado: R$ '))
# CÉDULAS R$50, R$20, R$10, R$1
cedula50 = cedula20 = cedula10 = cedula1 = 0
print('>>> A RETIRADA SERÁ DE:')
while True:
    if valor >= 50:
        valor = valor - 50
        cedula50 += 1
    elif valor >= 20:
         valor = valor - 20
         cedula20 += 1
    elif valor >= 10:
         valor = valor - 10
         cedula10 += 1
    elif valor >= 1:
        valor = valor - 1
        cedula1 += 1
    if valor == 0:
        break
print(f'{cedula50} cédulas de R$50' if cedula50 != 0 else '>')
print(f'{cedula20} cédulas de R$20' if cedula20 != 0 else '>')
print(f'{cedula10} cédulas de R$10' if cedula10 != 0 else '>')
print(f'{cedula1} cédulas de R$1' if cedula1 != 0 else '>')
