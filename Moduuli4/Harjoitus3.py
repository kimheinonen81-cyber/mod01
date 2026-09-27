pienin = None
suurin = None

syote = input("anna luku (tyhjä lopettaa): ")

while syote !="":
    luku = float(syote)

    if pienin is None or luku < pienin:
        pienin = luku

    if suurin is None or luku > suurin:
        suurin = luku

    syote = input("anna luku (tyhjä lopettaa): ")

print("Pienin luku:", pienin)
print("Suurin luku:", suurin)