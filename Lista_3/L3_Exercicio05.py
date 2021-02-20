def delta(a, b, c):
    ''' Calcula o delta de uma função de 2o graus de coeficientes a, b, c.
        Parâmetros:
            a - coeficiente real a
            b - coeficiente real b
            c - coeficiente real c
        Retorno:
            valor do delta (b*b - 4*a*c)
    '''
    # cálculo de delta
    res = b*b - 4*a*c
    # retorna delta
    return res


def temRaizes(a, b, c):
    ''' Determina o número de raízes de uma função de 2o graus de
        coeficientes a, b, c.
        Parâmetros:
            a - coeficiente real a
            b - coeficiente real b
            c - coeficiente real c
        Retorno:
            número inteiro de raízes da função de 2o grau
    '''
    d = delta(a, b, c)
    if d < 0:
        return 0
    elif d == 0:
        return 1
    else:
        return 2
    

# Programa principal
print('Função de 2o grau')
a = int(input('Digite o coeficiente real a: '))
b = int(input('Digite o coeficiente real b: '))
c = int(input('Digite o coeficiente real c: '))

if a != 0:
    print('∆ =', delta(a, b, c))
    raizes = temRaizes(a, b, c)
    if raizes == 0:
        print('Esta função não tem raizes reais.')
    elif raizes == 1:
        print('Esta função tem duas raizes reais iguais.')
    else:
        print('Esta função tem duas raizes reais distintas.')        
else:
    print('Não é uma função de 2o grau, pois a=0')

    
