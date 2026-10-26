#kirjoita funktio nimeltä keskiarvo, joka saa kolme kokonaislukuarvoa 
# (kokonaislukua) argumentteina.
#funktion tulee tulostaa näiden kolmen luvun matemaattinen ka.print
#Kysy luvut käyttäjältä input-funktion avulla

def keskiarvo(a, b, c):
    tulos = (a + b + c) / 3
    print("Lukujen keskiarvo on:", tulos)

luku1 = int(input("Anna ensimmäinen luku: "))
luku2 = int(input("Anna toinen luku: "))
luku3 = int(input("Anna kolmas luku: "))

keskiarvo(luku1, luku2, luku3)
