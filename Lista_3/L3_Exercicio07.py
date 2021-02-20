def dec2bin(n):
    ''' Realiza a conversão do número inteiro decimal n
        retornando seu equivalente binário.
        Parâmetros:
            n - número inteiro a ser convertido
        Retorno:
            string contendo a representação binária de n
    '''
    quociente = n
    binario = []
    while quociente > 0:
        resto = quociente % 2
        quociente = quociente // 2
        binario.insert(0, resto)
    return ''.join(map(str, binario))


# Programa principal
decimal = int(input('Digite um inteiro positivo: '))
binario = dec2bin(decimal)

print(f'({decimal})d <--> ({binario})b')
    
