# Funções parametrizadas

def ePar(valor):
    resultado = valor % 2 == 0  # testa se resto da divisão inteira por 2 é zero
    return resultado            # retorna resultado lógico (bool) do teste


def ePrimo(valor):
    if valor < 2: return False  # se valor menor que 2 não pode ser primo
    for i in range(2, valor):   # verifica divisão entre 2 e valor
        # testa se resto da divisão inteira de valor por i é zero (divisível)
        if valor % i == 0: return False
    return True                 # valor é primo


#
# Programa principal
#
print('Testes')
print('-------------------')
valor = int(input('Digite um inteiro positivo (>0): '))
print('-------------------')
# chamada de função, COM armazenamento do resultado
par = ePar(valor)
print(valor, 'é   par: ', par)

# chamada de função, SEM armazenamento do resultado
print(valor, 'é primo: ', ePrimo(valor))
