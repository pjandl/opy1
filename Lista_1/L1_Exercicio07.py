# Entrada de dados (leitura de valores)
precoEtanol = float(input('Preço do litro do etanol? '))
precoGasolina = float(input('Preço do litro da gasolina? '))

# Cálculos
precoTanqueEtanol = precoEtanol * 50
precoTanqueGasolina = precoGasolina * 50

eta_gas = precoEtanol / precoGasolina

etaEquiv = precoGasolina / precoEtanol

# Saída de dados (impressão)
print('      Tanque 50l Etanol =', precoTanqueEtanol)
print('    Tanque 50l Gasolina =', precoTanqueGasolina)
print('Relação Etanol/Gasolina =', eta_gas)
print('1 l Gasolina = ', etaEquiv, 'l Etanol')
