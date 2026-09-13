kuhan_mitta = float(input("Anna kuhan mitta senttimetreissä: "))
if kuhan_mitta < 37:
    puuttuva_mitta = 37 - kuhan_mitta
    print(f"Päästä kuha kasvamaan, se on {puuttuva_mitta:.2f} cm liian lyhyt")
if kuhan_mitta >= 37:
    print("Voit pitää kuhan.")