# Uso de decisão simples
precoIngresso = 22.00   # Preço do ingresso
descontoPadrao = 0.5    # Desconto padrão para estudantes (50%)

print('Compra de Ingressos')

quantidade = int(input('Quantos ingressos deseja comprar? '))
totalCompra = quantidade * precoIngresso

resp = input('Você é estudante [S|N]? ')

descontoCompra = 0          # Precisa definir variáveis para
totalFinal = totalCompra    # garantir execução OK nos dois casos

if resp=='S' or resp=='s':
    # Aplica desconto SE É estudante
    descontoCompra = descontoPadrao*totalCompra
    totalFinal = totalCompra - descontoCompra 

print('--------------------------------')
print('Quant ingressos =', quantidade)
print(' Preço ingresso = R$ {:7.2f}'.format(precoIngresso))
print('Total da compra = R$ {:7.2f}'.format(totalCompra))
print('       Desconto = R$ {:7.2f}'.format(descontoCompra))
print('    Total Final = R$ {:7.2f}'.format(totalFinal))
print('--------------------------------')
