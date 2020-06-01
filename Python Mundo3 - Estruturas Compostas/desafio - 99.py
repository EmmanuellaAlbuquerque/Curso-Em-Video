def maior(*números):
    print('-='*30, '\n', f'Analisando os valores passados...')
    print(f'{números} Foram informados {len(números)} valores ao todo.')
    if len(números) > 0:
        print(f'O maior valor informado é {max(números)}.')
    else:
        print(f'O maior valor informado é {0}.')


maior(1, 3, 5, 9)
maior(11, 5, 0, -1)
maior(1, 3)
maior()
maior(100, 1)
