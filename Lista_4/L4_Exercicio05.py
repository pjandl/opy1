import L4_Exercicio01 as ex1

def histograma(lista):
    ''' Cria um histograma com a lista de valores dados, considerando as
        faixas [0, 2), [2, 4), [4, 6), [6, 8), [8, 10].
    Parâmetros:
        lista - lista de valores reais entre 0 e 10.
    Retorno:
        lista contendo o número de ocorrëncias dos valores contidos na lista
        nas faixas pré-definidas.
    '''
    # cria lista contendo zero ocorrências para as cinco
    # faixas [0, 2), [2, 4), [4, 6), [6, 8), [8, 10]
    histo = [0, 0, 0, 0, 0]
    for v in lista:
        if v < 2:
            histo[0] += 1 # faixa [0, 2)
            # valores menores do que 0 também serão inclusos nesta faixa
        elif v < 4:
            histo[1] += 1 # faixa [2, 4)
        elif v < 6:
            histo[2] += 1 # faixa [4, 6)
        elif v < 8:
            histo[3] += 1 # faixa [6, 8)
        else:
            histo[4] += 1 # faixa [8, 10]
            # valores maiores do que 10 também serão inclusos nesta faixa
    return histo


# Programa principal
if __name__ == '__main__':
    print('Forneça 10 números reais entre 0 e 10')
    lista = ex1.listaReais(10)
    print('Valores dados:', lista)
    
    # determina histograma (distribuição dos valores nas faixas pré-definidas)
    ocorrências = histograma(lista)
-    # exibe resultados
    for i in range(0,5):
        print(f'Faixa [{i*2},{i*2+2:2}) = {ocorrências[i]:3}')    

