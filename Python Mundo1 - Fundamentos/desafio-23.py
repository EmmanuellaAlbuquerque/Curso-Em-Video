num = int(input('numero: '))
print('unidade: {}'.format(num%10))
num = num // 10
print('dezena: {}'.format(num%10))
num = num // 10
print('centena: {}'.format(num%10))
num = num // 10
print('milhar: {}'.format(num%10))

# OU:
# u = num // 1 % 10
# d = num // 10 % 10
# c = num // 100 % 10
# m = num // 1000 % 10
# print('unidade:{}\ndezena:{}\ncentena:{}\nmilhar:{}'.format(unidade,dezena,centena,milhar))

