# Adivinhe
# Um joguinho simples

import random

# Sorteia um inteiro entre 0 e 100
numeroSecreto = random.randrange(0, 101)

print('Adivinhe\nUm número entre 0 e 100')

numero = -1     # Inicializa número com valor inválido (fora da faixa)
tentativas = 0  # Contador de tentativas
while numero != numeroSecreto:
    # Lê palpite/tentativa do usuário
    numero = int(input('Seu palpite? '))
    tentativas += 1     # incrementa contador de tentativas
    # Verifica o palpite
    if numero < numeroSecreto:
        print('Baixo...')
    elif numero > numeroSecreto:
        print('Alto...')
    else:
        print('Você acertou!!!')
        
print('O número secreto era', numeroSecreto, '.')
print('Fim do jogo em', tentativas, 'tentativas.')
        
