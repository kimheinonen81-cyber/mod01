nimi = int(input("Kerro nimesi "))
if nimi == "Matti":
    print("Seuraava, kiitos!")
else:
    annos = int(input("montako keittoannosta halua: "))
    hinta = annos * 5.9
    print(f"Keittoannoksen hinta on {hinta:.2f} euroa")
    print("Seuraava kiitos")

    #koodissa virhe