# Funções com parâmetros variáveis

def mediaAritmetica(*a):
    quant = 0
    soma = 0
    for v in a:
        soma += v
        quant += 1
    if quant == 0: return    
    return soma / quant  # retorna média aritmética dos argumentos


def mediaGeometrica(*a):
    quant = 0
    produto = 1
    for v in a:
        produto *= v
        quant += 1
    if quant == 0: return    
    return produto**(1/quant) # retorna média geométrica dos argumentos


#
# Programa principal
#
print('Médias 2: parâmetros variáveis')
print('------------------------------')
print('Media Aritmetica =', mediaAritmetica())
print('Media Aritmetica =', mediaAritmetica(1))
print('Media Aritmetica =', mediaAritmetica(1, 2.0))
print('Media Aritmetica =', mediaAritmetica(1, 2.3, 4.6, 7.8))
print('------------------------------')
print('Media Geométrica =', mediaGeometrica())
print('Media Geométrica =', mediaGeometrica(1))
print('Media Geométrica =', mediaGeometrica(1, 2.0))
print('Media Geométrica =', mediaGeometrica(1, 2.3, 4.6, 7.8))
print('------------------------------')

