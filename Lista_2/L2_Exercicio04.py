# Entrada de dados (leitura de valores)
n = int(input('Número inteiro? '))

if n > 0:
    primo = True
    for i in range(2, n):
        if n % i == 0:
            primo = False
            break
    if primo:
        print(n, 'é primo')
    else:    
        print(n, 'não é primo')
else:    
    print(n, 'não pode ser testado como primo')
