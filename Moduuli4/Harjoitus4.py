import random
oikea_luku = random.randint(1, 10)
arvaus = int(input("Arvaa luku lukujen 1-10 väliltä: "))
while arvaus != oikea_luku:
    if arvaus < oikea_luku:
        print("Liian pieni luku")

    else:
        print("Liian suuri luku")

    arvaus = int(input("Arvaa uudelleen: "))

print("Oikein, onneksi olkoon, voitit, et mitään!!")
