sukupuoli = input("Anna sukupuolesi M/N: ")
hemoglobiini = int(input("Anna sinun hemoglobiiniarvosi: "))
if sukupuoli == "N" and hemoglobiini < 117:
    print("Hemoglobiinisi on liian matala")
elif sukupuoli == "N" and hemoglobiini > 175:
    print("Hemoglobiiniarvosi on liian korkea")
elif sukupuoli == "N" and hemoglobiini >=117 and hemoglobiini <=175:
    print("hemoglobiiniarvosi on viitekehyksen sisällä")

elif sukupuoli =="M" and hemoglobiini < 134:
    print("Hemoglobiinisi on liian matala")
elif sukupuoli =="M" and hemoglobiini > 195:
    print("Hemoglobiiniarvosi on liian korkea")
elif sukupuoli =="M" and hemoglobiini >=134 and hemoglobiini <=195:
    print("hemoglobiiniarvosi on viitekehyksen sisällä")

else:
    print("Virheellinen sukupuoli:")