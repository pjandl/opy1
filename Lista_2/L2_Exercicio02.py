# Entrada de dados (leitura de valores)
soma = 0        # somador de valores
quantidade = 0  # contador de valores

while soma < 100:
    n = float(input('Número real para somar? '))
    soma += n
    quantidade += 1

# Processamento (cálculo)
media = soma / quantidade

# Saída de dados (impressão)
print('Quantidade de valores: ', quantidade)
print('Soma dos valores: ', soma)
print('Média dos valores: ', media)
