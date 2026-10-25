sanat = ["auto", "polkupyörä", "talo", "tuotanto", "kissa", "tietokone"]

maara = 0

for sana in sanat:
    if len(sana) > 5:
        maara = maara + 1

print("Yli viisi kirjainta sisältäviä sanoja:", maara)