# Exemplo de uso de módulo

import conversores as tc # importação e renomeação do módulo
#
# Programa Simples
#
print("Conversão de Temperatura")
print("------------------------")
print("1. Celsius para Farenheit")
print("2. Celsius para Kelvin")
print("3. Farenheit para Celsius")
print("4. Fahrenheit para Kelvin")
print("5. Kelvin para Celsius")
print("6. Kelvin para Fahrenheit")
print("------------------------")
opcao = int(input('Opção [1..6]? '))
if opcao == 1 or opcao == 2:
    c = float(input('Temperatura C? '))
    if opcao == 1:
        # uso simples da função do módulo
        f = tc.celsiusToFahrenheit(c)
        print('{:.2f} C --> {:.2f} F'.format(c, f))
    else:
        k = tc.celsiusToKelvin(c)
        print('{:.2f} C --> {:.2f} K'.format(c, k))
elif opcao == 3 or opcao == 4:
    f = float(input('Temperatura F? '))
    if opcao == 3:
        c = tc.fahrenheitToCelsius(f)
        print('{:.2f} F --> {:.2f} C'.format(f, c))
    else:
        # uso combinado das funções do módulo
        k = tc.celsiusToKelvin(tc.fahrenheitToCelsius(f))
        print('{:.2f} F --> {:.2f} K'.format(f, k))
elif opcao == 5 or opcao == 6:
    k = float(input('Temperatura K? '))
    if opcao == 5:
        c = tc.kelvinToCelsius(k)
        print('{:.2f} K --> {:.2f} C'.format(k, c))
    else:
        f = tc.celsiusToFahrenheit(tc.kelvinToCelsius(k))
        print('{:.2f} K --> {:.2f} F'.format(k, f))
else:
    print('Opcao inválida!')
