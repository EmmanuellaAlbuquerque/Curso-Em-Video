# Modularização - Módulos
# Organização, Manutenção, Ocultação, Reutilização

def fatorial(n):
    f = 1
    for c in range(1, n+1):
        f *= c
    return f

def dobro(n):
    return n * 2


def triplo(n):
    return n * 3


# Pacotes - Bibliotecas (vários módulos separados por assunto)
# Quando um módulo fica pequeno demais, para muitos arquivos
# No pyCharm new -> Python Package

