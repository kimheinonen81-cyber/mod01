#luo ohjelma joka kysyy käyttäjältä hänen lempivärinsä. 
#Tarkista, löytyykö lempiväri ennalta määritetystä
#värilistasta ja vastaa sen mukaisesti
#Määrittele lista itse

varit = ["Punainen", "Keltainen", "Oranssi", "Musta"]
inputtti = input("kerro lempivärisi: ")
if inputtti in varit:
    print("väri löytyy listalta")
else:
    print("väriä ei löytynyt listalta")