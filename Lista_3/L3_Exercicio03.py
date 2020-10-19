'''
Função: ePrimo
Determina se número recebido como parâmetro é primo
Parâmetros:
    num - número a ser testado
Retorno:
    True - número é primo
    False - número não é primo
'''
def ePrimo(num):
    # testa divisão inteira de num por 2 até num-1
    for d in range(2, num):
        # verifica se num é dívisível por d
        if num % d ==0:
            # se divisível não é primo
            return False
    # não tem divisores entre 2 e num-2, é primo
    return True


# Programa principal
n = int(input('Digite um inteiro: '))
print(n, 'e primo? ', ePrimo(n))
