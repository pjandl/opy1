def palavras_distintas(frase):
    ''' Cria e retorna uma lista contendo palavras distintas da string dada.
        Parâmetros:
            frase - cadeia de caracteres cujas palavras serão listadas
        Retorno:
            lista de palavras distintas da string recebida
    '''
    # cria lista de palavras (con repetição) da string
    lista_palavras = frase.split(' ')
    palavras_distintas = set()
    for p in lista_palavras:
        palavras_distintas.add(p)
    return list(palavras_distintas)


def ocorrencias(frase):
    ''' Cria e retorna um dicionário contendo as palavras distintas da string
        e o número de sua ocorrência na frase dada.
        Parâmetros:
            frase - cadeia de caracteres cujas palavras terão as ocorrências
            contadas
        Retorno:
            dicionário contendo palavras distintas e seu número de ocorrências
            na frase recebida
    '''
    # cria lista de palavras (con repetição) da string
    lista_palavras = frase.split(' ')
    ocorrencias = {}
    for p in lista_palavras:
        if p in ocorrencias.keys():
            ocorrencias[p] += 1
        else:
            ocorrencias[p] = 1
    return ocorrencias
    

    
# Programa principal
if __name__ == '__main__':
    frase = input('Digite uma frase (sem símbolos de pontuação ou operadores):\n')
    palavras_distintas = palavras_distintas(frase)
    print('Lista de palavras distintas\n', palavras_distintas)
    ocorrencias = ocorrencias(frase)
    print('Ocorrências das palavras distintas\n', ocorrencias)

