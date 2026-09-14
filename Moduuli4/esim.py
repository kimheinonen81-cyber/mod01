komento = input("Anna uusi komento: ")

while komento!= "lopeta":
    if komento == "MAYDAY":
        break
    #tämä on toinen tapa lopettaa ohjelma
    print("Suoritetaan komento:", komento)
    komento = input("Anna uusi komento: ")
    #tämä on toinen tapa lopettaa ohjelma
else:
    print("Tämä on teksi elsen sisältä")

print("Ohjelma loppuu")