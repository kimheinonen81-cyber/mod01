#Indeksi alkaa nollasta

nimet = ["Viivi", "Ahmed", "Pekka", "Olga", "Mary"]
nimet2 = ["Mikko", "Teppo", "Seppo"]

nimet.append("Matti")
nimet.remove("Pekka")
nimet.insert(3, "Jaska")
nimet.extend(nimet2)
print(nimet)

print(nimet.index("Matti"))

if "Matti" in nimet:
    print("Matin indeksi on", nimet.index("Matti"))
else:
    print("Mattia ei löytynyt listalta")

#voidaan myös lajitella luvut.sort suuruusjärjestykseen
#pienimmästä isoimpaan

nimet.sort()
print(nimet)
#tähän ei tarvitse print(nimet+nimet2) koska ne on jo
#lisätty aikaisemmin extend komennolla