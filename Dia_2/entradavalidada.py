# Validação de entrada
# Quando é necessário ler um valor DENTRO de uma faixa de valores
MINIMO =  0.0   # valor mínimo da faixa (incluso)
MAXIMO = 10.0   # valor máximo da faixa (incluso)

# Entrada de dados
nota1 = float(input('Digite 1a nota [0.0, 10.0]: '))
# Validação: repete se nota1 FORA da faixa              
while nota1 < MINIMO or nota1 > MAXIMO:
    # Informa usuário sobre seu erro
    print('Êita! Vamos tentar novamente!')
    # Repete leitura
    nota1 = float(input('Digite 1a nota [0.0, 10.0]: '))
# Comando executado após laço, então nota1 ESTÁ na faixa

nota2 = float(input('Digite 2a nota [0.0, 10.0]: '))
# Validação: repete se valor FORA da faixa              
while nota2 < MINIMO or nota2 > MAXIMO:
    # Informa usuário sobre seu erro
    print('Êita! Vamos tentar novamente!')
    # Repete leitura
    nota2 = float(input('Digite 2a nota [0.0, 10.0]: '))
# Comando executado após laço, então nota2 ESTÁ na faixa
                  
# Saída de dados
media = (nota1 + nota2) / 2
print('Nota1: {:.1f} | Nota2: {:.1f} | Media {:.2f}'
      .format(nota1, nota2, media))
