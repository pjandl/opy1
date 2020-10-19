'''
Função: leInt
Lê valor inteiro na faixa indicada
Parâmetros:
    min - limite inferior (incluso)
    max - limite superior (incluso)
    msg - mensagem para usuário (opcional)
          padrao 'Digite um inteiro [{}...{}]'
Retorno:
    int - valor inteiro na faixa
'''
def leInt(min, max, msg='Digite um inteiro [{}...{}]: '):
    valor = int(input(msg.format(min, max)))
    while valor<min or valor>max:
        print('Fora da faixa!',end=' ')
        valor = int(input(msg.format(min, max)))
    return valor


# Programa principal
# Uso da função leInt
valor1 = leInt(1, 5)
valor2 = leInt(1, 5, 'Digite um outro inteiro entre {} e {}: ')

print('Valor 1 = ', valor1)
print('Valor 2 = ', valor2)
