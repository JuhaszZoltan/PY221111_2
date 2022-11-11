import random
szamok = []
for x in range(5):
    szamok.append(random.randint(0, 9))
print(f'számok: {szamok}')

# számok összege
sum = 0
for szam in szamok:
    sum += szam
print(f'számok összege: {sum}')

# számok átlaga
avg = sum/len(szamok)
print(f'számok átlaga: {avg}')

# páratlan számok darabszáma
count = 0
for szam in szamok:
    if szam % 2 == 1:
        count += 1
print(f'páratlan számok darabszáma: {count}')

# legnagybb szám indexe & legnagyobb szám
maxi = 0
for i in range(1, len(szamok)):
    if szamok[i] > szamok[maxi]:
        maxi = i
print(f'legnagyobb szám indexe: {maxi}')
print(f'a legnagyobb szám: {szamok[maxi]}')

# legkisebb szám indexe & legkisebb szám
mini = 0
for i in range(1, len(szamok)):
    if szamok[i] < szamok[mini]:
        mini = i
print(f'legkisebb szám helye: {mini}')
print(f'legkisebb szám: {szamok[mini]}')

# első átlagnál nem kisebb szám
i = 0
while szamok[i] < avg:
    i += 1
print(f'az első átlagnál nem kisebb elem: {szamok[i]}')

# van-e 3mal osztható szám?
i = 0
while i < len(szamok) and szamok[i] % 3 != 0:
    i += 1
if i < len(szamok): print('VAN 3-al osztható szám')
else: print('NINCS 3-al osztható szám')

# inputként bekért szám indexe