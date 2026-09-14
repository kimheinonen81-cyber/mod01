#while on alkuehdollinen toistorakenne
#huomaa järjestys, toistaa aina ylhäältä alaspäin
#Anna kolikoiden määrä ennen printtiä

#Alustetaan muuttujat / arvot:
kahvi = 5
kolikot = 0
#Ehto on kirjoitettu toistolausekkeeseen:
while kolikot < kahvi:
    #Tapa päivittää ehtoa
    kolikot += 1
    print("Annettu", kolikot, "kolikkoa")

print("Kiitos, kahvi on maksettu")