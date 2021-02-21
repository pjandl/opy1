import L4_Exercicio01 as ex1

# Programa principal
if __name__ == '__main__':
    print('Forneça uma lista de 20 valores reais')
    lista = ex1.listaReais(20)

    print('Lista dada :', lista)
    # lista auxiliar é uma cópia da lista
    aux = lista.copy()
    aux.sort() # ordena a cópia, não altera lista fornecida
    
    # maior valor é o último da lista ordenada (índice -1)
    print('Maior valor:', aux[-1])
    # função index indica a posição de elemento presente na lista
    print('Maior index:', lista.index(aux[-1]))
    # menor valor é o primeiro da lista ordenada (índice 0)
    print('Menor valor:', aux[0])
    # função index indica a posição de elemento presente na lista
    print('Menor index:', lista.index(aux[0]))

    # laço percorre lista para criar:
    impares = []    # lista de valores ímpares
    soma = 0        # soma de todos os valores
    positivos = 0   # soma de todos os valores positivos
    n_positivos = 0 # contagem dos valores positivos
    for e in lista:
        # verifica valores ímpares
        if e % 2 == 1:
            impares.append(e)
        # soma dos os valores
        soma += e
        # verifica valores positivos
        if e > 0:
            positivos += e
            n_positivos += 1

    print('Impares    : ', impares)
    print('Soma       : ', soma)
    print('Media      : ', positivos / n_positivos)
    
