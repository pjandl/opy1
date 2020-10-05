import math

# Entrada de dados (leitura de valores)
print('Equação de 2o grau: y = a*x^2 + b*x + c')
print('----------------------------')
a = float(input('Coeficiente a da equacao? '))
b = float(input('Coeficiente b da equacao? '))
c = float(input('Coeficiente c da equacao? '))
print('----------------------------')

# Processamento e saida dos dados (cálculos e impressão)
if a == 0:
    print('a == 0! Não é equação de 2o grau!')
else:
    delta = math.pow(b,2) - 4*a*c
    if delta == 0:
        x = -b / (2*a)
        print('Raízes Iguais\n| x1 = x2 =', x)
    elif delta > 0:
        x1 = (-b + math.sqrt(delta))/ (2*a)
        x2 = (-b - math.sqrt(delta)) / (2*a)
        print('Raízes Diferentes\n| x1 =', x1, '\n| x2 =', x2)
    else:
        print('delta < 0! Raízes complexas1')
