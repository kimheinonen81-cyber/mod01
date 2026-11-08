
def poista_parittomat(luvut):
    parilliset = []

    for luku in luvut:
        if luku % 2 == 0:
            parilliset.append(luku)

    return parilliset

alkuperainen = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

uusi_lista = poista_parittomat(alkuperainen)

print(f"Alkuperäinen lista: {alkuperainen}")
print(f"Parilliset luvut: {uusi_lista}")
