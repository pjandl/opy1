'''
Nome:             situacao
Propósito:        Verifica situação de aprovação numa disciplina
Parâmetros:       nota(float), frequencia(float), carga horária(int)
                  média aprovação(float=6.0), frequência aprovação(float=0.75)
Valor de retorno: int 0 (aprovado), 1 (reprov. nota),
                  2 (reprov. falta) ou 3 (reprov. nota e falta 
'''
def situacao(nota, freq, CH, MAp=6.0, FAp=.75):
    situacao = 0
    if nota<MAp:
        situacao += 1
    if (freq/CH)<FAp:
        situacao += 2
    return situacao


#
# Programa principal
#
print('Situação de Aprovação')
print('-------------------')
nota = float(input('Digite sua nota (real): '))
freq = int(input('Digite suas presenças (inteiro: '))
ch = int(input('Digite carga horária (inteiro: '))
print('-------------------')
print('Padrão: média 6.0 e 75% freq. mínima')
print('Situação: ', situacao(nota, freq, ch))
print('-------------------')
print('Especial: média 5.0 e 80% freq. mínima')
print('Situação: ', situacao(nota, freq, ch, 5.0, 0.8))
print('-------------------')

