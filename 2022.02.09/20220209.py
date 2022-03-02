from math import *
#--------------------------------------------------------------#
#I                      Új feladat                            I#
#--------------------------------------------------------------#
def feladat1(szam):
    if szam<16:
        print("A szám 10-szerese:", szam*10)
    else:
        print("A szám harmada:", round(szam/3,2))
#--------------------------------------------------------------#
#I                      Új feladat                            I#
#--------------------------------------------------------------#
def feladat2(szam):
    print("A bekért szám:", szam)
    if szam%2==0:
        print("A szám adata:")
        print("A szám páros")
    else:
        print("A szám adata:")
        print("A szám páratlan")
#--------------------------------------------------------------#
#I                      Új feladat                            I#
#--------------------------------------------------------------#
def feladat3(szam):
    if 10<szam<50:
        if szam//10==1:
            print("tizesek")
        elif szam//10==2:
            print("Huszasok")
        elif szam//10==3:
            print("Harmincasok")
        else:
            print("Negyvenesek")
    else:
        print("A szám nem esik 10 és 50 közé")
#--------------------------------------------------------------#
#I                      Új feladat                            I#
#--------------------------------------------------------------#
def feladat4(szam):
    if 12<szam<25:
        if szam%2==0:
            print("A bekért szám:", szam)
            print("A szám páros")
        else:
            print("A bekért szám:", szam)
            print("A szám páratlan")
    else:
        print("A szám nem esik 12 és 25 közé.")

    print("A másik megoldás:")
    if 12<szam<25 and szam%2==0:
        print("A szám páros")
    else:
        print("A szám nem felelt meg az elvártnak, nem páros, és nem 12 és 25 között található.")
#--------------------------------------------------------------#
#I                      Új feladat                            I#
#--------------------------------------------------------------#
def feladat5(szam):
    szamok= int(2,3,5,7)
    if szam%szamok==0:
        print("A bekért szám:", szam)
        print("A szám oszható az alábbiak közül valamelyikkel: 2,3,5,7")
    else:
        print("A bekért szám:", szam)
        print("A szám nem osztható az alábbiak közűl semmelyikkel: 2,3,5,7")
#--------------------------------------------------------------#
#I                      Új feladat                            I#
#--------------------------------------------------------------#
def feladatc1():
    for i in range(1,18):
        print(i*3, end=" ")
#--------------------------------------------------------------#
#I                      Új feladat                            I#
#--------------------------------------------------------------#
def feladatc2():
    for i in range(1,17):
        print(pow(2,i), end=" ")
#--------------------------------------------------------------#
#I                      Új feladat                            I#
#--------------------------------------------------------------#
def feladatc3():
    for i in range(1,6):
        for j in range(1,16):
            print(i*j, end=" ")
        print()
#--------------------------------------------------------------#
#I                      Új feladat                            I#
#--------------------------------------------------------------#
def feladatc4():
    for i in range(1,26):
        if i*7%4==0:
            print(i*7, end=" ")
    print()
#--------------------------------------------------------------#
#I                      Új feladat                            I#
#--------------------------------------------------------------#
def feladatc5():
    a=3
    b=3
    c=5
    print("a=",a, "b=",b, "c=",c,"V=",a*b*c)
    for i in range(1,5):
        a=a+1
        b=b+2
        c=c+3
        print("a=",a, "b=",b, "c=",c, "V=",a*b*c)
#--------------------------------------------------------------#
#I                      Új feladat                            I#
#--------------------------------------------------------------#
def feladatc6():
    for i in range(15,93):
        print(i, end=" ")
#--------------------------------------------------------------#
#I                      Új feladat                            I#
#--------------------------------------------------------------#
def feladatc7():
    for i in range(100,401):
        if i%4==0:
            print(i, end=" ")
#--------------------------------------------------------------#
#I                      Új feladat                            I#
#--------------------------------------------------------------#
def feladatc8():
    for i in range(-100,101):
        if i%9==0:
            print(i, end=" ")
#--------------------------------------------------------------#
#I                      Új feladat                            I#
#--------------------------------------------------------------#
def feladatc9():




    

#--------------------------------------------------------------#
#I--[]                  Főprogram                         []--I#
#--------------------------------------------------------------#
"""szam=int(input("Kérek egy számot!:"))"""

#feladat1(szam)
#feladat2(szam)
#feladat3(szam)
#feladat4(szam)
#feladat5(szam) ---- Hibás
#feladatc1()
#feladatc2()
#feladatc3()
#feladatc4()
#feladatc5()
#feladatc6()
#feladatc7()
#feladatc8()
feladatc9()
#feladatc10()