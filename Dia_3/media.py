# Funções parametrizadas

import math

def mediaAritmetica(a, b):
    resultado = (a + b) / 2
    return resultado        # retorna a média aritmética de a e b


def mediaGeometrica(a, b):
    resultado = math.sqrt(a*b)
    return resultado        # retorna a média geométrica de a e b


#
# Programa principal
#
print('Médias')
print('-------------------')
valor1 = float(input('Valor real 1? '))
valor2 = float(input('Valor real 2? '))
print('-------------------')
media = mediaAritmetica(valor1, valor2)
print('Media Aritmetica({:.2f},{:.2f}) = {:.2f}'
      .format(valor1, valor2, media))

print('Media Geometrica({:.2f},{:.2f}) = {:.2f}'
      .format(valor1, valor2, mediaGeometrica(valor1, valor2)))

