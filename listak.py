#           0         1        2        3         4     
nevek = ['Gábor', 'Vilmos', 'Adél', 'Klaudia', 'Dénes']

print(f'3-mas indexű elem: {nevek[3]}')
print(f'a nevek 2. eleme: {nevek[1]}')
elemek_szama = len(nevek)
print(f'elemek száma: {elemek_szama}')
print(f'utolsó index: {len(nevek) - 1}')

i:int = int(input('hányas indexű elemet szeretnéd cserélni? '))
nev:str = input('mire? ')
nevek[i] = nev
print(f'nevek: {nevek}')

nev:str = input('új név a lista végére: ')
nevek.append(nev)
print(f'nevek: {nevek}')

i:int = int(input('hová szeretnél beszúrni új elemet? '))
nev = input('milyen nevet? ')
nevek.insert(i, nev)
print(f'nevek: {nevek}')

nev = input('melyik nevet szeretnéd törölni? ')
nevek.remove(nev)
print(f'nevek: {nevek}')

i = int(input('honnan szeretnél törölni? '))
nevek.pop(i)
print(f'nevek: {nevek}')

list.sort(nevek)

for nev in nevek:
    print(f'{nev}', end=' ')
print('\n')
for i in range(len(nevek)):
    print(f'nevek[{i}]: {nevek[i]}')