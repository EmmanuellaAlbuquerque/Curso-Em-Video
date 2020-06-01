def notas(*notas, situação=False):
    '''
    -> Função para analisar notas e situações de vários alunos.
    :param notas: Uma ou mais notas dos alunos (aceita várias)
    :param situação: valor opcional, indicando se deve ou não adicionar a situação no dicionário
    :return: dicionário com várias informações sobre a situação da turma.
    '''
    aluno = dict()
    # - QUANTIDADE DE NOTAS
    aluno['qNotas'] = len(notas)
    # - A MAIOR NOTA
    aluno['maiorNota'] = max(notas)
    # - A MENOR NOTA
    aluno['menorNota'] = min(notas)
    # - A MÉDIA DA TURMA
    aluno['média'] = 0
    for nots in notas:
        aluno['média'] += nots
    aluno['média'] = aluno['média']/len(notas)
    # - A SITUAÇÃO (OPCIONAL)
    if situação:
        if aluno['média'] >= 7:
            aluno['situação'] = 'Aprovado'
        elif aluno['média'] < 4:
            aluno['situação'] = 'Reprovado'
        elif 4 <= aluno['média'] < 7:
            aluno['situação'] = 'Recuperação'
    return aluno


print(notas(5.5, 9.5, 10, 6.5))
print(notas(7, 7, 7, situação=True))
print(notas(5, 5, 5, situação=True))
