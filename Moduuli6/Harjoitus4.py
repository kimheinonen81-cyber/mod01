
def laske_summa(luvut):
    summa = 0

    for luku in luvut:
        summa = summa + luku

    return summa

numerot = [2, 4, 6, 8]

tulos = laske_summa(numerot)

print(f"Lukujen summa on {tulos}")
