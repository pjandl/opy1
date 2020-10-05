# Entrada de dados (leitura de valores)
dec = int(input('Número inteiro decimal? '))

# Processamento (conversão)
bin = ''
quoc = dec

while quoc > 0:
    bin = str(quoc%2) + bin
    quoc = quoc // 2

print('Decimal(',dec,') <--> Binário(', bin, ')')    
