def contaCaracteres(cadeia,caractere):
    ''' Realiza a contagem do número de ocorrências do caractere indicado
        na cadeia de caracteres (string) dada.
        Parâmetros:
            n - número de ocorrências do caractere
        Retorno:
            string contendo a representação binária de n
    '''
    ocorrencias = 0
    for c in cadeia:
        if c == caractere:
            ocorrencias += 1
    return ocorrencias


# Programa principal
cadeia = input('Digite uma cadeia de caracteres: ')
caractere = input('Digite um caractere a ser contado na cadeia dada: ')

n_ocorrencias = contaCaracteres(cadeia, caractere)
print(f'Foram encontradas {n_ocorrencias} de "{caractere}" em "{cadeia}".')
    
