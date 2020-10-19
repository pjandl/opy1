import math

# Função que lê um ponto x,y retornando-o como uma tupla
def lePonto(nomePonto):
    x = float(input('{:s}.coordenada x? '.format(nomePonto)))
    y = float(input('{:s}.coordenada y? '.format(nomePonto)))
    return (x, y) # cria e retorna uma tupla com valores de x e y


# Função que calcula a distância no eixo X entre dois pontos p1 e p2
def deltaX(p1, p2):
    delta = abs(p1[0] - p2[0])
    return delta


# Função que calcula a distância no eixo Y entre dois pontos p1 e p2
def deltaY(p1, p2):
    delta = abs(p1[1] - p2[1])
    return delta


# Função que calcula a distância entre dois pontos p1 e p2
def distancia(p1, p2):
    return math.sqrt(deltaX(p1, p2)**2 + deltaY(p1, p2)**2)


# Programa principal
ponto1 = lePonto('Ponto 1')
ponto2 = lePonto('Ponto 2')

print('Distancia entre {:s} e {:s} é {:.3f}.'
      .format(str(ponto1), str(ponto2), distancia(ponto1, ponto2)))

