# opções
listaOpcoes = ['Localizar chave-valor', 'Alterar chave-valor',
               'Remover chave-valor', 'Adicionar chave-valor', 'Sair', ]
# define dicionario vazio
dicionario = {}

# função localizar
def localizar():
    chave = input('Qual chave-valor quer localizar? ')
    if chave in dicionario:
        print('Valor associado', dicionario[chave])
    else:
        print('Chave não localizada')
    return


# função alterar
def alterar():
    chave = input('Qual chave-valor quer localizar? ')
    if chave in dicionario:
        valor = input('Qual novo valor da chave? ')
        dicionario[chave] = valor
        print('Novo valor associado')
    else:
        print('Chave não localizada')
    return


# função remover
def remover():
    chave = input('Qual chave-valor quer localizar? ')
    if chave in dicionario:
        valor = dicionario.pop(chave)
        dicionario[chave] = valor
        print('Valor associado removido: ', valor)
    else:
        print('Chave não localizada')
    return


# função adicionar
def adicionar():
    chave = input('Qual nova chave? ')
    valor = input('Qual valor associado? ')
    dicionario[chave] = valor
    print('Novo par chave-valor criado')


# Menu
while True:
    print('=====')
    print(dicionario)
    print('=====')
    for o in range(0, len(listaOpcoes)):
        print('{:d}.{:s}'.format(o, listaOpcoes[o]))
    opcao = int(input('Opção? '))
    if opcao == 0:
        localizar()
    elif opcao == 1:
        alterar()
    elif opcao == 2:
        remover()
    elif opcao == 3:
        adicionar()
    else:
        break
    
