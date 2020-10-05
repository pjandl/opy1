# Entrada de dados (leitura de valores)
larguraSalao = int(input('Largura do salão (m)? '))
comprimentoSalao = float(input('Comprimento do salão (m)? '))

larguraPiso = float(input('Largura do piso (mm)? '))
comprimentoPiso = float(input('Comprimento do piso (mm)? '))

# Cálculos
pecasLargura = int((1000 * larguraSalao) // larguraPiso) + 1
pecasComprimento = int((1000 * comprimentoSalao) // comprimentoPiso) + 1

totalPecas = pecasLargura * pecasComprimento

# Saída de dados (impressão)
print('No peças para largura     =', pecasLargura)
print('No peças para comprimento =', pecasComprimento)
print('Total de Pecas            =', totalPecas)

