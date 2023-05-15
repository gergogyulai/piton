import random

szamok=[]
db = 0
for szám in range(5):
    vélSzám = random.randint(100,200)
    szamok.append(vélSzám)
    if vélSzám > 150:
        db+=1
print(szamok)
print(db)
print(len(szamok))