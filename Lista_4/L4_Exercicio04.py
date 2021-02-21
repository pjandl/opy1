# Observe que TODAS as conversões solicitadas já estão disponíveis
# como construtores dos tipos embutidos list, set e tuple.

def lista2tupla(lista):
    ''' Retorna uma tupla com os elementos da lista dada. '''
    return tuple(lista)


def lista2conjunto(lista):
    ''' Retorna um conjunto com os elementos da lista dada. '''
    return set(lista)


def tupla2lista(tupla):
    ''' Retorna uma lista com os elementos da tupla dada. '''
    return list(tupla)


def conjunto2lista(conjunto):
    ''' Retorna uma lista com os elementos do conjunto dado. '''
    return list(conjunto)


# Programa principal
if __name__ == '__main__':
    # uma lista inicial
    lista = [1, 2, 3]
    print(lista, type(lista))

    # lista para tupla
    objeto = lista2tupla(lista)
    print(objeto, type(objeto))

    # tupla para lista
    objeto = tupla2lista(objeto)
    print(objeto, type(objeto))

    # lista para conjunto
    objeto = lista2conjunto(objeto)
    print(objeto, type(objeto))

    # conjunto para lista
    objeto = conjunto2lista(objeto)
    print(objeto, type(objeto))

    # compara lista inicial com objeto
    print('lista == objeto?', lista == objeto)

