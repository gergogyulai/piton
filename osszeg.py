import random

szamok=[]
for szám in range(5):
    szamok.append(random.randint(1,10))
print(szamok)

összeg = 0
for szám in szamok:
    összeg = összeg + szám
print(összeg)
print("A lista elemeinek összege:", összeg)
print("A lista elemeinek ", összeg,"az összege.")
print("A lista elemeinek ", összeg," az összege.", sep='')
print(f"A lista elemeinek az összege: {összeg}")
print(sum(szamok))