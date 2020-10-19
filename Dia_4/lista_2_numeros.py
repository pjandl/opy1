# opções
listaOpcoes = ['Localizar número', 'Alterar número',
               'Remover número', 'Adicionar número', 'Sair', ]
# define lista vazia
listaNumeros = []

# função localizar
def localizar():
    valor = float(input('Qual valor quer localizar? '))
    for i in range(0, len(listaNumeros)):
        if listaNumeros[i] == valor:
            print('Valor localizado na posição', i)
            return
    print('Valor não localizado')
    return


# função alterar
def alterar():
    pos = int(input('Qual posicao quer alterar? '))
    if pos>=0 and pos<len(listaNumeros):
        valor = float(input('Qual novo valor? '))
        listaNumeros[pos] = valor
        print('Valor alterado na posição', pos)
    else:
        print('Posição inválida')
    return


# função remover
def remover():
    pos = int(input('Qual posicao quer remover? '))
    if pos>=0 and pos<len(listaNumeros):
        valor = listaNumeros.pop(pos)
        print('Valor', valor, 'removido da posição', pos)
    else:
        print('Posição inválida')
    return


# função adicionar
def adicionar():
    valor = float(input('Qual novo valor? '))
    listaNumeros.append(valor)


# Menu
while True:
    print('=====')
    print(listaNumeros)
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
    
