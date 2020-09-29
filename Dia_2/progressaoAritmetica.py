# Testa se três inteiros formam uma progressão aritmética ou geométrica
print ('Progressão Aritmética ou Geométrica')

a = float(input('Digite um inteiro a: '))
b = float(input('Digite um inteiro b: '))
c = float(input('Digite um inteiro c: '))

# se a distância/diferença entre a e b é a mesma que entre b e c,
# temos um PA (progressão aritmética)
if b-a == c-b:
    print('a, b e c formam uma Progressão Aritmética de razão {:.2f}.'
          .format(b-a))
else:
    print('a, b e c NÃO formam uma Progressão Aritmética.')
    
# se a ou b tiverem valor zero, não é possível que seja
# uma progressão geométrica, então finaliza o programa
if a==0 or b==0: exit()

# se a proporção/razao entre a e b é a mesma que entre b e c,
# temos um PG (progressão geométrica)
if b/a == c/b:
    print('a, b e c formam uma Progressão Geométrica de razão {:f}.'
          .format(b/a))
else:
    print('a, b e c NÃO formam uma Progressão Geométrica.')
    

