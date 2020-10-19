# coleções
pares = set()   # conjunto (lista sem repetição) de valores pares
impares = set() # conjunto (lista sem repetição) de valores ímpares
numeros = []    # relação (lista) de valores digitados

print('--COLEÇÕES--')
# entrada de dados
while True:
    valor = int(input("Valor inteiro [0 ou negativo finaliza]: "))
    # Verifica fim
    if valor < 1:
        break
    # inclui valor na lista de números
    numeros.append(valor)
    # separa valores pares dos ímpares
    if valor % 2 == 0:
        pares.add(valor)
    else:
        impares.add(valor)
    # impressão das coleções
    print('    Números:{}'.format(numeros))
    print('      Pares:{}'.format(pares))
    print('    Ímpares:{}'.format(impares))
    print('Par+Ímpares:{}'.format(pares|impares))

print('--  FIM  ---')
