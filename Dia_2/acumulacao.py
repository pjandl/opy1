# Acumulação de valores de entrada
# Leitura de N valores a serem somados, com indicação da média
N = 10  # número de valores

# Entrada de dados
soma = 0    # variável para acumulação, recebe valor nêutro
contador = 0    # variável de controle da repetição
while contador < N:
    # Solicita valor
    valor  = float(input('Digite valor real #{:d}: '
                         .format(contador+1)))
    # Acumula valor
    soma += valor # o mesmo que: soma = soma + valor
    # Incrementa variável de controle
    contador += 1 # o mesmo que: contador = contador + 1

                  
# Saída de dados
media = soma / N
print('Soma: {:.2f} | Media {:.2f}'.format(soma, media))
