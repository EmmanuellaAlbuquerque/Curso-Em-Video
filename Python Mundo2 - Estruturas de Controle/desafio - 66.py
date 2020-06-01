numero = soma = count = 0
while True:
    numero = int(input('Digite o número desejado, [999 p/ parar]: '))
    if numero == 999:
        break
    count += 1
    soma += numero
print(f'Foram digitados {count} NÚMEROS e a SOMA entre eles é {soma}.')
