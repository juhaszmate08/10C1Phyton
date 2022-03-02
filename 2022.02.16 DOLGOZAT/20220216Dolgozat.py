def feladat1():
    a=int(input("Kérek egy valós számot, hogy kiírjam a 3-szorosát!:"))
    print("A valós szám 3 szorosa:", a*3)
    print()
#-------------------------------------------------------#
def feladat2():
    h=int(input("Add meg a háromszög egyik oldalát!: "))
    k=int(input("Add meg a háromszög másik olkdalát!: "))
    print("A háromszög területe:")
    print(h*k//2, "Cm2")
    print()
#-------------------------------------------------------#
def feladat3():
    b=int(input("Kérek egy számot, hogy megvizsgáljam a szám osztahtó-e 5-el!:"))
    if b%5==0:
        print("A szám oszható öttel")
    else:
        print("A szám NEM oszható 5-el!")
    print()
#-------------------------------------------------------#
def feladat4():
    c=int(input("Adj meg egy számot, hogy megvizsgáljam hogy -50 és 20 között van-e!:"))
    if -50<c<20:
        print("A megadott szám, -50 és 20 között található!")
    else:
        print("A megadott szám NEM esik -50 és 20 közé, vagy egyenlő -50-el és 20-al")
    print()
#-------------------------------------------------------#
def feladat5():
    print("Az első 20 négyzetszám:")
    for i in range(1,21):
        print(i*i, end=" ")
    print()
#-------------------------------------------------------#        
def feladat6():
    print("Azok a számok melyek 3-al osztva 2 maradékot adnak! (1-től 20-ig)")
    for i in range(1,21):
        if i%3==2:
            print(i, end=" ")
    print()
#-------------------------------------------------------# 
def feladat7():
    print("A 9-es szorzótábla első 25 eleme:")
    for i in range(1,218,9):
        print(i, end=" ")
    print()
#-------------------------------------------------------# 

#Főprogram
feladat1()
feladat2()
feladat3()
feladat4()
feladat5()
feladat6()
feladat7()