# Cálculo do IMC (índice de massa corpórea)
print('IMC::índice de massa corpórea')

# Entrada de dados
altura = float(input('Digite sua altura em metros (m): '))
massa = float(input('Digite sua massa em quilogramas (kg): '))

# Processamento
imc = massa / (altura**2);

#Saída de dados
print('IMC =', imc)
print('IMC = {:.2f}'.format(imc))
