# Adivinhe
# Um joguinho simples

import random

# Sorteia um inteiro entre 0 e 20
numeroSecreto = random.randrange(0, 21)

print('Adivinhe\nUm número entre 0 e 20')

numero = -1     # Inicializa número com valor inválido (fora da faixa)
tentativas = 0  # Contador de tentativas
while numero != numeroSecreto:
    # Lê palpite/tentativa do usuário
    numero = int(input('Seu palpite? '))
    tentativas += 1     # incrementa contador de tentativas
    # Verifica o palpite
    if numero != numeroSecreto:
        print('Você não acertou...')
    else:
        print('Você acertou!!!')
        
print('O número secreto era', numeroSecreto, '.')
print('Fim do jogo em', tentativas, 'tentativas.')
        
