#1$ = 3,8772zł
from forex_python.converter import CurrencyRates
c = CurrencyRates() #przypisanie do zmiennej c funkcji biblioteki

print("Którą podajesz walutę? Jeśli zł napisz zl jesli dolar napisz $")
waluta = input()
if waluta == "zl":
    print("ile złotówek chcesz zamienić na dolary?")
    zloty = float(input())
    dolar = c.convert('PLN', 'USD', zloty) #użycie funkcji biblioteki, która służy do zamiany walut w obecnym kursie
    print("za to dostaniesz tyle", dolar, "$")
else:
    print("ile dolarów chcesz zamienić na złotówki?")
    dolar = float(input())
    zloty = c.convert('USD', 'PLN', dolar)
    print("za to dostaniesz tyle", zloty, "zł")