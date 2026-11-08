
import math

def laske_yksikkohinta(halkaisija, hinta):
    sade = halkaisija / 2 / 100
    pinta_ala = math.pi * sade ** 2
    return hinta / pinta_ala

print("Pizza 1")
halkaisija1 = float(input("Anna pizzan halkaisija (cm): "))
hinta1 = float(input("Anna pizzan hinta (€): "))

print("Pizza 2")
halkaisija2 = float(input("Anna pizzan halkaisija (cm): "))
hinta2 = float(input("Anna pizzan hinta (€): "))

yksikkohinta1 = laske_yksikkohinta(halkaisija1, hinta1)
yksikkohinta2 = laske_yksikkohinta(halkaisija2, hinta2)

print(f"Pizza 1: {yksikkohinta1:.2f} €/m²")
print(f"Pizza 2: {yksikkohinta2:.2f} €/m²")

if yksikkohinta1 < yksikkohinta2:
    print("Pizza 1 antaa paremman vastineen rahalle.")
elif yksikkohinta2 < yksikkohinta1:
    print("Pizza 2 antaa paremman vastineen rahalle.")
else:
    print("Pizzat ovat yhtä edullisia.")
