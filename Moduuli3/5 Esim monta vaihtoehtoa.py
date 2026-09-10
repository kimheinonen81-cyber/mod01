#Monta vaihtoehtoa -> elif - haara (else if)
#Näitä voi olla rajaton määrä

ika = int(input("Anna ikäsi: "))
if ika >= 65:
    print("Olet eläkkäällä, vanhus!")
elif ika >= 18:
    print(" Olet työikäinen, mene töihin!")
elif ika >= 7:
    print("Mene kouluun")
else:
    print("Olet kakara")