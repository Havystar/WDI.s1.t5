#1$ = 3,8772zł

print("Którą podajesz walutę? Jeśli zł napisz zl jesli dolar napisz $")
waluta = input()
if waluta == "zl":
    print("ile złoówek chcesz zamienić na dolary?")
    zloty = float(input())
    dolar = float(zloty/3.8772)
    print("za to dostaniesz tyle", dolar, "$")
else:
    print("ile dolarów chcesz zamienić na złoówki?")
    dolar = float(input())
    zloty = float(dolar*3.8772)
    print("za to dostaniesz tyle", zloty, "zł")