print('Lista de Nomes')
# define tamanho da lista
MAX = 5
# define uma lista vazia
nomes = []


# entrada dos nomes
print('Digite', MAX, 'nomes')
for i in range(1, MAX+1):
    umNome = input(str(i) + '.Nome? ')
    nomes.append(umNome)
    print(nomes, ':', len(nomes)) # len obtém o tamanho da lista


# recuperação de nomes
i = int(input('Qual nome deseja? [0..{:d}]'.format(MAX-1)))
while i >= 0 and i < MAX:
    print(i, ':', nomes[i])
    i = int(input('Qual nome deseja? [0..{:d}]'.format(MAX-1)))

print('Tchau!')    
