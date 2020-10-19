# dados
cor = input('Carro - cor: ')
marca = input('Carro - marca: ')
modelo = input('Carro - modelo: ')

# dicionário
# uma forma de definir
dict1 = {'cor':cor, 'marca':marca, 'modelo':modelo}

dict2 = {} # outra forma de definir
dict2['cor'] = cor
dict2['marca'] = marca
dict2['modelo'] = modelo

# impressão de chaves e valores
print('dict1')
for k in dict1.keys():
    print('{}:{}'.format(k, dict1[k]))

print('dict2')
for k in dict1.keys():          
    print('{}:{}'.format(k, dict2[k]))

