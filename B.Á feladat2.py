import random

lista=[]
szamlalo = 0

for i in range(10):
    szam = random.randint(1000,2000)
    lista.append(szam)
    if szam > 1500:
        szamlalo += 1

print(f"{lista} Az összes generált szám")
print(f"Ennyi 1500-nál nagyobb szám van {szamlalo}")