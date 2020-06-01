def voto(nasc):
    # Escopo de importação
    from datetime import datetime
    idade = datetime.now().year - nasc
    print(f'Com {idade} anos: ', end='')
    # VOTO NEGADO
    if idade < 16:
        return 'VOTO NEGADO/NÃO VOTA'
    # VOTO OPCIONAL
    elif 16 <= idade < 18 or idade > 65:
        return 'VOTO OPCIONAL'
    # VOTO OBRIGATÓRIO
    else:  # idade >= 18:
        return 'VOTO OBRIGATÓRIO'


nascimento = int(input('Em que ano você nasceu? '))
print(voto(nascimento))
