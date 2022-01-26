from math import *
from random import *

def feladat1_5():
    a= "alma"
    print(type(a))

    b= "w"
    print(type(b))

    c= 5
    print(type(c))

    d= 1.5
    print(type(d))

    e= True
    print(type(e))
#---------------------------------------------------------------#
def feladat6_9():

    a= input("Kérek egy szót!:")
    print(a)
    print()

    b= input("Kérek egy mondatot!:")
    print(b)
    print()

    c= input("Kérek egy karaktert!:")
    print(c)
    print()

    d= int(input("Kérek egy egész számot!:"))
    print(d)
    print()
#---------------------------------------------------------------#
def feladat10():
    valosszam= float(input("Kérek egy valós számot!:"))
    print(valosszam)
    print(valosszam, "x", "2" "=", valosszam*2)
    print("Pi *", valosszam, "=", pi*valosszam)
    print("Hamradik hatványa:", pow(valosszam,3))
    print("A szám négyzetgyöke:", sqrt(valosszam))
    print("gyöke, két tizedesre kerekítve", round(sqrt(valosszam),2))
#---------------------------------------------------------------#
def feladat_11_16():
    veletlenszam= randint(10,50)
    print(veletlenszam)

    veletlen= randint(1,10)
    print(veletlen)

    veletlenvalos= random()
    print(veletlenvalos)

    veletlenn= randrange(10,51)
    print(veletlenn)

    egesz= int(input("Kérek egy egész számot:"))
    if egesz%2==0:
        print("A szám páros")
    else:
        print("a szám páratlan")

    if egesz>0:
        print("A szám pozitív")
    elif egesz<0:
        print("A szám negatív")
    else:
        print("A szám 0")

    if egesz>30:
        print("A szám nagyobb mint 30")
    else:
        print("A szám nem nagyobb mint 30")

    egyik= int(input("Kérek egy egész számot:"))
    masik= int(input("kérek egy másik egész számot:"))
    if egyik > masik:
        print("A nagyobb szám:", egyik)
    elif egyik<masik:
        print("A nagyobb szám:", masik)
    else:
        print("A két szám egyenlő")
    print("A kissebb szám:", min(egyik,masik))
    print("a nagyobb szám:", max(egyik,masik))


#Főprogram
#feladat1_5()
#feladat6_9()
#feladat10()
feladat_11_16()