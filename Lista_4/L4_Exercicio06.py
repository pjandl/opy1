def cria_dicio_aluno(prompt='Aluno'):
    ''' Colhe dados (RA, disciplina, P1, P2, média, frequência) de um aluno
        e retorna um dicionário contendo tais dados.'
        Parâmetros:
            prompt - texto complementar de mensagem para usuário
        Retorno:
            dicionário com dados colhidos
    '''
    # dicionário para conter dados de um aluno
    dicio = {}
    # entrada de dados: RA, disciplina, P1, P2, frequência
    dicio['RA'] = input(prompt + ' [RA]? ')
    dicio['DISC'] = input(prompt + ' [Disciplina]? ')
    dicio['P1'] = float(input(prompt + ' [Nota P1]? '))
    dicio['P2'] = float(input(prompt + ' [Nota P2]? '))
    # média pode ser calculada
    dicio['MEDIA'] = (dicio['P1'] + dicio['P2']) / 2
    dicio['FREQ'] = int(input(prompt + ' [Frequência]? '))
    # retorna o dicionário
    return dicio


def exibe_dicio_aluno(dicio, prefixo=''):
    ''' Exibe chaves e valores do dicionário dado, uma par chave/valor
        por linha.
        Parâmetros:
            dicio - dicionário com dados colhidos
            prefixo - string com prefixo de impressão
        Retorno:
            None
    '''
    for k in dicio:
        print(f'{prefixo}{k:20} = {dicio[k]}')
    return


# Programa principal
if __name__ == '__main__':
    # Cria dicionário de dados de aluno
    aluno = cria_dicio_aluno()
    # Exibe dados do dicionário do aluno
    print('Aluno')
    exibe_dicio_aluno(aluno)

