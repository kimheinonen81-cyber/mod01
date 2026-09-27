oikea_tunnus = "nakki"
oikea_salasana = "muki"

yritykset = 0

while yritykset < 5:
    tunnus = input("Käyttäjätunnus: ")
    salasana = input("Salasana: ")
    if tunnus == oikea_tunnus and oikea_salasana:
        print("Tervetuloa")
        break

    yritykset +=1

if yritykset >=5:
    print("Pääsy evätty, mene takaisin sinne mistä tulit")