# Função simples 
'''
Nome:             Linha
Propósito:        imprimir uma linha no console
Parâmetros:       não tem
Valor de retorno: não tem
'''
def Linha():
    print('=======================================')
    return


#
# Programa "principal" segue após as definições das funções
#
print('Exemplo de Programa com Função Simples')
# chamada da funcao Linha()
Linha()
print('Funções podem ser acionadas várias vezes')
for i in range(0, 5):
    print(i,".",sep='',end='')
    Linha()

print('Final do programa')
Linha()
