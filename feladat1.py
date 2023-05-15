import random

#10 db véletlenszám generálása 100 és 200 között egy listába


lista = []
for szám in range(10):
    vélSzám=random.randint(100,200)
    lista.append(vélSzám)
print(lista)



#írjuk ki a lista elmeinek összegét!

összeg=0
for szám in lista:
    összeg += szám
print(f"A lista elemeinek összege: {összeg}")

#ebben a listában hány darab 2-vel osztható szám van?

darab = 0
for szám in lista:
    if szám % 2 == 0:
        darab += 1
print(f"2-vel osztható számok: {darab}")

#írjuk ki a lista legnagyobb elemét!
legnagyobb = 100
for szám in lista:
    if szám > legnagyobb ==
    print(f"a legnagyobb szám: {legnagyobb}")

        
#írjuk ki a lista legkisebb elemét!
legkisebb = 200
for szám in lista:
    if szám < legnagyobb ==
    print(f"A legkisebb szám: (legkisebb}")
#írjuk ki a lista elemeinek átlagát!

