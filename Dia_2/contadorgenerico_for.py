# Contador genérico com repetição automática

# Entrada de dados
inicio = int(input('Valor inteiro inicial da contagem: '))
final = int(input('Valor inteiro final (> inicio) da contagem: '))
passo = int(input('Valor inteiro do passo da contagem: '))

# processamento de dados
print('início')
soma = 0    # variável para acumulação dos valores da contagem
# função range parametrizada com as variáveis acima
for i in range(inicio, final, passo):
    print('|', i)   # comando a ser repetido
    soma += i       # o mesmo que soma = soma + i

# saída de dados
print('fim')
print('Soma = ', soma)

