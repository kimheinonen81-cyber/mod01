#continue käsky
summa = 0

while True:
    num = int(input("Anna numero, -1 lopettaa: "))

    if num == - 1:
        break

    if num >= 10:
        continue

    summa += num

print("Summa on:", summa)