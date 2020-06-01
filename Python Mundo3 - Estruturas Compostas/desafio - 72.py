# Números entre 0 e 20 por extenso

contagem = ('Zero', 'Um', 'Dois', 'Três', 'Quatro', 'Cinco', 'Seis', 'Sete', 'Oito', 'Nove', 'Dez', 'Onze', 'Doze', 'Treze', 'Quatorze', 'Quinze',
            'Dezesseis', 'Dezessete', 'Dezoito', 'Dezenove', 'Vinte')
# print(contagem)
print('{:-^50}'.format(' NÚMEROS POR EXTENSO '))
while True:
    numero = int(input('Digite o número inteiro ENTRE 0 e 20: '))
    while numero < -1 or numero > 20:  # Ou com While True: if 0 <= num <= 20
        numero = int(input('Você digitou um número inválido.\nTente Novamente[número inteiro ENTRE 0 e 20]: '))
    print(f'O numero {numero} por extenso é {contagem[numero]}.')

    desejaContinuar = str(input('Digite s p/ continuar e n p/ parar\: ')).strip().upper()
    while desejaContinuar not in 'SN':
        desejaContinuar = str(input('Digite s p/ continuar e n p/ parar\: ')).strip().upper()
    if desejaContinuar == 'N':
        print('{:-^51}'.format(' PROGRAMA ENCERRADO COM SUCESSO! '))
        break
