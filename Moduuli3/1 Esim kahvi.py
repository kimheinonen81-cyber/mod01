raha = float(input("Kuinka paljon sinulla on rahaa? "))
if raha >= 5:
    print("Voit ostaa kahvin.")
else:
    print("Rahat ei riitä, suksi kuuseen")
    print("Sinulta puuttuu", 5-raha, "mene töihin!")

print("Hyvää päivänjatkoa!")