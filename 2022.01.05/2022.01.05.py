from random import *
from math import *


def feladat31():
    for i in range(10,101):
        if i %7 ==3:
            print(i, end=" ")
print()

# [X]>>-----------------------------------------<<[X]
# III                ÚJ FELADAT                   III
# [X]>>-----------------------------------------<<[X]

def feladat32():
    szovegeslista=[]
    szovegeslista.append('alma')
    szovegeslista.append("körte")
    szovegeslista.append("szilva")
    szovegeslista.append("sárgabarack")
    szovegeslista.append("eper")
    print('A lista elemeinek száma:', len(szovegeslista))
    print(szovegeslista)
    for item in szovegeslista:
        print(item, end=" ")
    print()

# [X]>>-----------------------------------------<<[X]
# III                ÚJ FELADAT                   III
# [X]>>-----------------------------------------<<[X]

def feladat34():
    karakterlista=[]
    karakterlista.append("c")
    karakterlista.append("2")
    karakterlista.append("b")
    karakterlista.append("4")
    karakterlista.append("a")
    for item in karakterlista:
        print(item, end=" ")
print() 

# [X]>>-----------------------------------------<<[X]
# III                ÚJ FELADAT                   III
# [X]>>-----------------------------------------<<[X]

def feladat36():
    egeszlista=[2,3,4,5,6]
    egeszlista.append(randint(0,100))
    egeszlista.append(int(input("Kérek egy számot:")))
    for i in range(5):
        egeszlista.append(randint(0,100))
    for item in egeszlista:
        print(item, end=" ")
print()

# [X]>>-----------------------------------------<<[X]
# III                ÚJ FELADAT                   III
# [X]>>-----------------------------------------<<[X]

def feladat40():
    veletlenek=[]
    for i in range(15):
        veletlenek.append(randint(10,51))
    for item in veletlenek:
        print(item, end=" ")
    print()
    print("A legnagyobb szám:", max(veletlenek))
    print("A legkisebb szám:", min(veletlenek))
    print("A számok összege:", sum(veletlenek))

# [X]>>-----------------------------------------<<[X]
# III                ÚJ FELADAT                   III
# [X]>>-----------------------------------------<<[X]

#a. a számokat egymás mellé szóközzel elválasztva
#b. a legnagyobb számot
#c. a legkisebb számot
#d. a számok összegét
#e. a számok átlagát
#f. a számok terjedelmét (legnagyobb-legkisebb)
#g. gyűjtd ki listába vagy tömbbe a párosokat
#h. a párosokat egymás mellé szóközzel elválasztva
#i. a párosok darabszámát
#j. a párosok összegét
#k. a párosok átlagát
#l. a párosok terjedelmét
#m. a legnagyobb páros számot!

def feladatkerdezos():
    szamok=[]
    paros=[]
    for i in range(15):
        szamok.append(randint(10,50))
    for item in szamok:
        print(item, end=" ")
    print()
    print("Legnagyobb szám:", max(szamok))
    print("Legkisebb szám:", min(szamok))
    print("A számok összege:", sum(szamok))
    print("A számok átgala:", )
    print("A számok terjedelme:", )
#                          Páros Számok részleg
    print("Páros számok:")
    for item in szamok:
        if item % 2 == 0:
            paros.append(item)
    for item in paros:
        print(item, end=" ")
    print()

    print("A páros számok darabszáma:")
    for item in paros:
        print(len(paros), end=" ")
    print()


#-------------------------------------------------------------------------------------------------------------------
#                                              Itt kezdődik a főprogram
#             ___      ___ 
#feladat31()  II\\    //II               
#feladat32()  II \_\/_/ II         
#feladat34()  II        II       
#feladat36()  II        II      
#feladat40()
feladatkerdezos()