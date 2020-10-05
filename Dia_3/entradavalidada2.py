# Validação de entrada com função

'''
Nome:             LeituraValidada
Propósito:        Efetua leitura validada na faixa [MINIMO,MAXIMO]
Parâmetros:       não tem
Valor de retorno: real
'''
MINIMO =  0.0   # valor mínimo da faixa (incluso)
MAXIMO = 10.0   # valor máximo da faixa (incluso)

def LeituraValidada():
    nota = float(input('Digite a nota [{:.1f},{:.1f}]: '
                            .format(MINIMO,MAXIMO)))
    while nota < MINIMO or nota > MAXIMO:
        # Informa usuário sobre seu erro
        print('Valor inválido! Repita por favor.')
        # Repete leitura
        nota = float(input('Digite a nota [{:.1f},{:.1f}]: '
                            .format(MINIMO,MAXIMO)))
    # Comando executado após laço, então nota1 ESTÁ na faixa
    return nota     # retorno de valor (a nota)


#
# Programa principal
#
# Entrada de dados
nota1 = LeituraValidada()
nota2 = LeituraValidada()
                  
# Saída de dados
media = (nota1 + nota2) / 2
print('Nota1: {:.1f} | Nota2: {:.1f} | Media {:.2f}'
      .format(nota1, nota2, media))
