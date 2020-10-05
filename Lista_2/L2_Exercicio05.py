# Entrada de dados (leitura de valores)
somaPos = 0     # somador de valores positivos
quantPos = 0    # contador de valores positivos
somaNeg = 0     # somador de valores negativos
quantNeg = 0    # contador de valores negativos

# Entrada inclui processamento (soma e contagem)
while True:
    n = float(input('Número real para somar? '))
    if n > 0:
        somaPos += n
        quantPos += 1
    elif n < 0:
        somaNeg += n
        quantNeg += 1
    else:
        break

# Pós-processamento dos dados (cálculos)
mediaPos = somaPos / quantPos
mediaNeg = somaNeg / quantNeg

# Saída de dados (impressão)
print('Quantidade de valores positivos: ', quantPos)
print('Quantidade de valores negativos: ', quantNeg)
print('Soma dos valores positivos: ', somaPos)
print('Soma dos valores negativos: ', somaNeg)
print('Média dos valores positivos: ', mediaPos)
print('Média dos valores negativos: ', mediaNeg)
