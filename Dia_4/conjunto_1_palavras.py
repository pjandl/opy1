# Cria conjunto de palavras
def criaConjunto():
    conjunto = set()    # conjunto vazio
    palavra = input('Digite uma palavra (enter finaliza): ')
    while len(palavra) > 0:
        print(conjunto,'<--',palavra)
        conjunto.add(palavra)
        palavra = input('Digite uma palavra (enter finaliza): ')
    print(conjunto)
    return conjunto


# Programa principal
A = criaConjunto()  # cria um conjunto de palavras A
B = criaConjunto()  # cria um conjunto de palavras B

# Operações sobre os conjuntos
print('União A | B:', A | B)
print('-----------:', A.union(B))

print('Intersecção A & B:', A & B)
print('-----------------:', A.intersection(B))

print('Diferença A - B:', A - B)
print('---------------:', A.difference(B))
print('Diferença B - A:', B - A)
print('---------------:', B.difference(A))
        
print('Diferença simétrica A ^ B:', A ^ B)
print('-------------------------:', A.symmetric_difference(B))
print('Diferença simátrica B ^ A:', B ^ A)
print('-------------------------:', B.symmetric_difference(A))
