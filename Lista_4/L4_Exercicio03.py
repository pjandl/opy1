import math as m

def pontoR2(prompt='Digite coordenada real'):
    ''' Realiza a leitura coordenada x,y de ponto no plano cartesiano R².
    Parâmetros:
        prompt - mensagem a ser exibida
    Retorno:
        tupla contendo coordenada (x, y)
    '''
    x = float(input(prompt + ' x ? '))
    y = float(input(prompt + ' y ? '))
    return (x, y)


def distancia(p1, p2):
    ''' Calcula a distância entre dois pontos p1 e p2 fornecidos como tuplas
        de valores numéricos reais.
    Parâmetros:
        p1 - primeiro ponto no plano cartesiano R²
        p2 - segundo ponto no plano cartesiano R²
    Retorno:
        valor real que corresponden à distância entre p1 e p2
    '''
    # calcula distância entre dois pontos usando o teorema de Pitágoras
    d =  m.sqrt(m.pow(p1[0] - p2[0], 2) + m.pow(p1[1] - p2[1], 2))
    return d
    

# Programa principal
if __name__ == '__main__':
    print('Forneça três coordenadas')
    p1 = pontoR2()
    p2 = pontoR2()
    p3 = pontoR2('Último ponto')

    # calcula distância entre os pontos p1, p2 e p3
    d1_2 = distancia(p1, p2)
    print('Distancia p1-p2 =', d1_2)
    d2_3 = distancia(p2, p3)
    print('Distancia p1-p2 =', d2_3)
    d3_1 = distancia(p3, p1)
    print('Distancia p1-p2 =', d3_1)

    # determina perímetro do triângulo formado
    perimetro = d1_2 + d2_3 + d3_1
    print('Perímetro formado é', perimetro, '.')
    print(f'Perímetro formado é {perimetro:.3f}.')
    print('Perímetro formado é {:.2f}.'.format(perimetro))
    
