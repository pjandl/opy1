'''
Função: ePar
Determina se número recebido como parâmetro é par ou ímpar.
Parâmetros:
    num - número a ser testado
Retorno:
    True - número é par
    False - número é ímpar
'''
def ePar(num):
    # verifica resto da divisão inteira de num por 2
    if num % 2 == 0:
        # resto 0 --> é par
        return True
    else:
        # resto 1 --> é ímpar
        return False


# Programa principal
n = int(input('Digite um inteiro: '))
par = ePar(n)
print(n, 'e par? ', par)
print(19, 'e par? ', ePar(19))
print(64, 'e par? ', ePar(64))
