from math import *
from random import *
#--------------------------------------------------------------------#
#--------------------------------------------------------------------#
#-------------------------------------------------------------#
#Az első feladat, a,b,c,d,e,f,g,h
def feladat1():
    listam=[]
    paratlan=0
    for i in range(10):
        listam.append(randint(1,100))
    print(listam)
    print()
#-------------------------------------------------------------#
#a, feladat
    print("'a', feladat:")
    for item in listam:
        print(item, end=" ")
    print()
#-------------------------------------------------------------#
#b feladat
    print("'b', feladat:")
    print()
#-------------------------------------------------------------#
#c feladat
    print("'c', feladat:")
    print()
#-------------------------------------------------------------#
#d feladat
    print("'d', feladat:")
    print("Legnagyobb szám a listában:", max(listam))
    print()
#-------------------------------------------------------------#
#e feladat
    print("'e', feladat:")
    print("Legkisebb szám a listában:", min(listam))
    print()
#-------------------------------------------------------------#
#f feladat
    print("'f', feladat:")
    print()
#-------------------------------------------------------------#
#g feladat
    print("'g', feladat:")
    for item in listam:
        if item%3==0:
            paratlan +=1
    print("A páratlanok összege:", paratlan)
    print()
#-------------------------------------------------------------#
#h feladat
    print("'h', feladat:")
    print()
#--------------------------------------------------------------------#
#--------------------------------------------------------------------#
#-------------------------------------------------------------#


#-------------------------------------------------------------#
#A második feladat a,b,c,d,e
def feladat2():
    mondat=input("Kérlek adj meg egy mondatot!:")
    print(mondat)
    print("Az 'e' betű előfordulás száma:")
    print(mondat.count("e"))
#-------------------------------------------------------------#
#A harmadik feladat
def feladat3():
    szam=int(input("Adj meg egy számot, azt amely hónapra kiváncsi vagy!(1,12 között):" ))
    honapok= ["január","február","március","április","május","június","július","augusztus","szeptember","október","november","december"]
    if 0<szam<13:
        print(honapok[szam-1])
    else:
        print("A szám nem felel meg az 1-12 kért számnak!")
#-------------------------------------------------------------#

#-------------#
#I főprogram I#
#-------------#
feladat1()
feladat2()
feladat3()