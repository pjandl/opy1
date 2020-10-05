# Uso Função de geração de valor para dado

import random

'''
Nome:             dado
Propósito:        Gera um valor aleatório entre [1,6]
Parâmetros:       não tem
Valor de retorno: int
'''
def dado():
    numero = random.randrange(1,7)
    return numero     # retorno de valor (numero "obtido" no dado)

#
# Programa principal
#
print('Lançamento de Dados')
print('-------------------')
dado1 = dado()
dado2 = dado()
print('dado1 :', dado1,'\ndado2 :', dado2)
print('-------------------')
if dado1+dado2 == 7:
    print('Sete! Você ganhou!')
elif dado1+dado2 == 12:
    print('Doze! Você está com sorte!')
else:
    print('Boa tentativa.')
