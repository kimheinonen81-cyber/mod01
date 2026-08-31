#kysytään käyttäjältä
pituus = float(input("Anna pituutesi: "))
paino = float(input("Anna painosi: "))

bmi = paino / (pituus / 100) **2
print (f"bmi:si on, {bmi:10.2f}")
#huomaa desimaalit f kirjaimella