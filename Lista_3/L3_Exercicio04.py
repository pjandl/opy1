def soma(n):
    ''' Soma os inteiros de 0 até n (incluso)
        Parâmetros:
            n - inteiro limite da soma            
        Retorno:
            inteiro contendo soma de 0 até n (incluso)
    '''
    # inicializa soma
    soma = 0
    for v in range(1, n+1):
        soma += v
    # retorna soma
    return soma


# Programa principal
n = int(input('Digite um inteiro: '))
print('soma de 0 até', n, '=', soma(n))

