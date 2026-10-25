tuntipalkka = float(input("Anna tuntipalkka: "))
tunnit = float(input("Anna tehdyt tunnit: "))
viikonpaiva = input("Anna viikonpäivä: ")

if viikonpaiva.lower() == "sunnuntai":
    palkka = tuntipalkka * tunnit * 2
else:
    palkka = tuntipalkka * tunnit

print(f"Päiväpalkka on {palkka:.2f} euroa")