# Entrada de dados (leitura de valores)
n = int(input('Número inteiro para tabuada? '))


# Saída de dados (impressão)
print('for:')
for i in range(0, 10+1):
    print(n, 'x', i, '=', n*i)

print('while:')
i = 0
while i <= 10:
    print(n, 'x', i, '=', n*i)
    i += 1
