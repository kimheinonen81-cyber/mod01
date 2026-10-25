tuotteet = []
maarat = []

while True:
    tuote = input("Mitä tuotetta valmistetaan? ")
    maara = int(input("Kuinka monta valmistetaan? "))

    tuotteet.append(tuote)
    maarat.append(maara)

    vastaus = input("Jatketaanko tuotantoa? ")

    if vastaus == "Ei":
        break

print("Tuotanto lopetettu!")
print("Valmistetut tuotteet:")

for i in range(len(tuotteet)):
    print(tuotteet[i], ":", maarat[i], "kpl")