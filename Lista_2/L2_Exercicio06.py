# Entrada de dados (leitura de valores)
print('Equação da reta: y = a*x + b')
print('----------------------------')
a = float(input('Coeficiente a da reta? '))
b = float(input('Coeficiente b da reta? '))
print('----------------------------')

# Processamento e saida dos dados (cálculos e impressão)
x = -5.0
print('| {:4s} | {:8s} |'.format('x', 'y'))
print('+------+----------+')
while x <= +5.0:
    y = a*x + b
    print('| {:4.1f} | {:8.3f} |'.format(x, y))
    x += 0.5
print('+------+----------+')
