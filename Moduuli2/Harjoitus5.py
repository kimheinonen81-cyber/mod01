leiviskat = int(input("Anna leiviskät: "))
naulat = int(input("Anna naulat: "))
luodit = int(input("Anna luodit: "))
leiviskat_luoteina  = leiviskat * 20 * 32
naulat_luoteina = naulat * 32
luodit_yhteensa = leiviskat_luoteina + naulat_luoteina + luodit
grammat_yhteensa = luodit_yhteensa * 13.3
kilogrammat = int(grammat_yhteensa // 1000)
grammat = grammat_yhteensa % 1000
print(f"Massa on {kilogrammat} kilogrammaa ja {grammat:.0f} grammaa.")