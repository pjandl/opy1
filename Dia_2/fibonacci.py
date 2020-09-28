# Fibonacci
# Sequência (série) matemática dada por F(n) = F(n-1) - F(n-2)
# que significa: cada elemento é a soma dos dois valores anteriores
# Assim se definem os dois primeiros elementos como: F(0) = 0 e F(1) = 1
# Assim: 0 1 1 2 3 5 8 13 21 34 55 89

n = int(input('Digite o número do elemento: '))

v_2 = 0     # valor inicial do 2o anterior
v_1 = 1     # valor inicial do 1o anterior

print("F(0) = 0\nF(1) = 1")

for i in range(2, n+1):
    v = v_1 + v_2   # o termo  atual é a soma dos dois anteriores
    print('F({:d}) = {:d} + {:d} = {:d}'.format(i, v_1, v_2, v))
    
    v_2 = v_1       # o 2a anterior se torna o 1o anterior
    v_1 = v         # o 1a anterior se torna atual
    
print("----------")
print("F({:d}) = {:d}".format(n, v))
