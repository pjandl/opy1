# Contador regressivo com repetição automática

inicio = 10         # valor inicial é dez
final  =  0         # valor final é zero
passo  = -2         # valor do passo é negativo (contagem regressiva)

# função range parametrizada com as variáveis acima
for i in range(inicio, final, passo):
    print(i)        # comando a ser repetido

# função range parametrizada com as variáveis acima
# final-1 inclui o valor final (numa contagem regressiva)
for i in range(inicio, final-1, passo):
    print(i)        # comando a ser repetido    




