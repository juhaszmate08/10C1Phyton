from random import *
listam=[]
'''#elemekszama=int(input("Hány szám legyen?:"))
elemekszama=10
for i in range(0,elemekszama):
    listam.append(randint(1,100))
print(listam)
print(listam[0])
print(listam[-1]) #az utolsó elem
print(listam[0:4]) #0-tól 4-ig a listaba
print(listam[2:5]) #2-től 5-ig a listaba
print(listam[7:]) #7-től felfelé mind
print(listam[:5]) #elejétől az 5-ig
listam[5]= 'alma'
print(listam)

for item in listam:
    print(item, end=" ")

print()
print(len(listam)) #elemek száma
print()
print(listam.index('alma')) #az alma helye, indexe

listam.pop()
print(listam)
listam.pop(3) #törli a 3-ast
print(listam)
listam.remove('alma') #törli az almát
print(listam)
#listam.clear() #csak az lista elmeket törli
print(listam)
listam.reverse() #fordított sorrend
print(listam)
listam.sort() #sorba rendez
print(listam)
listam.insert(3,'körte')
print(listam)'''

"""
def feladat1():
    elemszam=int(input("kérem az elemek számát!:")):
    szamok=[]
    for i in range(1,elemszam):
        szamok.append(randint(1,50))
    print(szamok)
    prl=0
    for item in szamok:
        if item%2==1:
            prl+=1
    print("A páratlanok száma:", prl)
feladat1()"""

"""def feladat2():
    #Olvass be egy pár számot (ha kell, a darabszámot is kérje be a program), majd írd ki a párosok összegét!
    szam=int(input("Kérem az elemek számát:"))
    szamok=[]
    for i in range (1,szam):
        szamok.append(randint(1,100))
    print(szamok)
    prsz=0
    for item in szamok:
        if item %2==0:
            prsz+=item
    print("A páros számok száma=", prsz)
feladat2()
"""
def feladat3():
    szam=int(input("Kérem az elemek számát:"))
    szamok=[]
    for i in range (1,szam):
        szamok.append(randint(1,50))
    print(szamok)
    prsz=0
    for i in range(0,len(szamok)):
        if szamok[i] %2==0:
            print(szamok[1],"sorszáma:", i+1)


feladat3()

#                                    HÁZI
"""5. Olvass be egész számokat egy tömbbe/listába (ha kell, a darabszámot is kérje 
be a program), majd kérj be egy egész számot, és mondd meg, hogy hányszor 
szerepel a tömbben.
6. Olvasd be egy tömbbe/listába az osztály tanulóinak keresztneveit (ha kell, a 
darabszámot is kérje be a program). Mondd meg, hogy egy adott keresztnevű 
tanulóból hány jár az osztályba (a keresett nevet is kérje be a program)."""










