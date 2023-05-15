import random

szamok=[]
for szam in range(5):
    szamok.append(random.randint(1,10))
print(szamok)

osszeg = 0
for szam in szamok:
    osszeg = osszeg + szam
print(osszeg)
átlag = osszeg / len(szamok)
print(f"A lista átlaga: {átlag}")