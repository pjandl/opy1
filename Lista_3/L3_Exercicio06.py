def lerReal(minimo, maximo, prompt='Digite um valor real', tentativas=3):
    ''' Lê uma valor real dentro da faixa especificada.
        Parâmetros:
            minimo - limite inferior da faixa de valores reais aceita (incluso)
            maximo - limite superior da faixa de valores reais aceita (incluso)
            prompt - mensagem exibida para usuário
            tentativas - número máximo de tentativas
        Retorno:
            valor real dentro da faixa;
            None se o número de tentativas for excedido ou
            a faixa de valores for inválida (minimo >= maximo).
    '''
    if minimo >= maximo:
        return None
    leituras = 0;
    while leituras < tentativas:
        valor = float(input(prompt + f' [De {minimo} até {maximo}]? '))
        if minimo <= valor and valor <= maximo:
            return valor
        leituras -= 1
        print('Valor inválido!')
    return None


# Programa principal
v = lerReal(0, 10, tentativas=2)
print('Primeiro Valor lido:', v)

v = lerReal(0, 10, prompt='Outro valor real')
print('Segundo Valor lido:', v)

v = lerReal(0, 10, prompt='Mais um valor real', tentativas=4)
print('Terceiro Valor lido:', v)    
