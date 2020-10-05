# Módulo com funções de conversão

# conversores de temperatura
def celsiusToFahrenheit(c):
    return 9 * c / 5 + 32


def fahrenheitToCelsius(f):
    return 5 * (f - 32) / 9


def celsiusToKelvin(c):
    return c + 273


def kelvinToCelsius(k):
    return k - 273


# conversores de volume
def litrosToGaloes(l):
    return l * 0.264172


def galoesToLitros(g):
    return g * 3.78541

