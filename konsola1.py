import math

temperature = input(" Powiedz czy podajesz temperature w fahrenheitach (fa) czy celsjuszach (ce): ")

if temperature == "fa":
    fahrenheit_temperature = float(input("Podaj temperature w Fahrenheitach: "))
    celsius = (fahrenheit_temperature - 32)* 5 / 9
    print (f"{fahrenheit_temperature} stopni Fahrenheita to {celsius} stopni Celsjusza.")
elif temperature == "ce":
    celsius_temperature = float(input("Podaj temperature w Celsjuszasz: "))
    fahrenheit = (celsius_temperature * 9/5)+32
    print (f"{celsius_temperature} stopni Celsjusza to {fahrenheit} stopni Fahrenheita.")