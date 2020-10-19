import random

'''
Testa acertos na palavra secreta
'''
def verificaAcerto(palavra, letra, tentativa):
    posicao = 0
    letrasAcertadas = 0
    for l in palavra:
        if letra.lower() == l.lower():
            tentativa[posicao] = letra
        if tentativa[posicao] == palavra[posicao]:
            letrasAcertadas += 1
        posicao += 1
    return len(palavra) == letrasAcertadas

# preparação
# define uma lista de palavras "secretas"
palavras = ['Python', 'banana', 'ideia', 'elemento', 'zebra']
# sorteia uma palavra e "organiza" tentativa
segredo = palavras[random.randrange(0, len(palavras))].lower()
tentativa = []
for i in range(0, len(segredo)):
    tentativa.append('_')
enforcado = False
acertou = False
erros = 0
print('Mini-Forca')

# entrada das letras
while (not enforcado and not acertou):
    letra = input('Digite uma letra: ')
    if letra in segredo:
        acertou = verificaAcerto(segredo, letra, tentativa)
    else:
        erros += 1
        print('Você errou!', erros, 'erro(s).')
    print(len(segredo)*'-----')    
    print(tentativa)
    print(len(segredo)*'-----')
    enforcado = erros == 4

# situação final
if acertou:
    print('Você venceu!')
else:
    print('Você foi enforcado!')
