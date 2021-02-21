def listaReais(n):
    ''' Realiza a leitura de n valores reais, retornando uma lista
        com os valores lidos.
    Parâmetros:
        n - número de valores reais que quevem ser lidos
    Retorno:
        lista contendo n valores reais
    '''
    lista = []
    for i in range(n):
        valor = float(input(f'Digite o {i+1}o valor real: '))
        lista.append(valor)
    return lista


# Programa principal
if __name__ == '__main__':
    print('Forneça uma lista de 5 valores reais')
    lista = listaReais(5)

    print('Lista fornecida', lista, sep='\n')
    
