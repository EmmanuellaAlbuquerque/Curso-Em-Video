# Conversão Temperatura
# (X°C × 9/5) + 32 = 32 °F

temperatura = float(input('Informe a temperatura em °C: '))
conversao = (temperatura*(9/5)+32)
print('A temperatura de {}°C corresponde a {}°F!'.format(temperatura, conversao))