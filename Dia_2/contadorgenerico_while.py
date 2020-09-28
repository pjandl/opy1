# Contador genérico com repetição condicional

# Entrada de dados
inicio = float(input('Valor real inicial da contagem: '))
final = float(input('Valor real final da contagem: '))
passo = float(input('Valor real do passo da contagem: '))

                    # variável de controle é i
i = inicio          # valor inicial é inicio

# processamento de dados
print('início')
while i <= final:   # fim da contagem (não incluído) é final
    print('|', i)   # comando a ser repetido
    i += passo      # incremento determinado por passo

# saída de dados
print('fim')

