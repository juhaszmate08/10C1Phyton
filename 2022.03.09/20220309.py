from math import *
from random import *
#-------------------------------------------------------------------#
def feladat1():
    f=open("elsoiras.txt", "w", encoding=("UTF8"))
    f.write("alma" + "\n")
    f.writelines("Körte" + "\n")
    f.writelines("szilva" + "\n")
    f.close()
#-------------------------------------------------------------------#
def feladat2():
    f=open("szamok10ig.txt", "w", encoding="UTF8")
    for i in range(1,11):
        if i<10:
            f.write(str(i)+", ")
        else:
            f.write(str(i))
    f.close()
#-------------------------------------------------------------------#
def feladat3():
    f=open("szamokegymasalatt.txt", "w", encoding="UTF8")
    for i in range(1,11):
        if i<10:
            f.write(str(i)+"\n")
        else:
            f.write(str(i))
    f.close()
#-------------------------------------------------------------------#
def feladat4():
    f=open("elsotiznegyzetszam.txt", "w", encoding="UTF8")
    for i in range(1,11):
        if i<10:
            f.write(str(i**i)+"\n")
        else:
            f.write(str(i**i))
    f.close()
#-------------------------------------------------------------------#
def feladat5():
    f=open("harmasfeladat.txt", "w", encoding="UTF8")
    for i in range(10):
        if i<9:
            f.write(str(randint(100,201))+"\n")
        else:
            f.write(str(randint(100,201)))
    f.close()
#-------------------------------------------------------------------#
def feladat6():
    f=open("negyesfeladat.txt", "w", encoding="UTF8")
    for i in range(15):
        if i<14:
            f.write(str(randint(1,5)) + "\n")
        else:
            f.write(str(randint(1,5)))
    f.close()
#-------------------------------------------------------------------#
def feladat7():
    f=open("otosfeladat.txt", "w", encoding="UTF8")
    for i in range(28):
        if i<27:
            f.write(str(randint(35,45)) + "\n")
        else:
            f.write(str(randint(35,45)))
    f.close
#-------------------------------------------------------------------#
def feladat8():
    f=open("hatosfeladat.txt", "w", encoding="UTF8")
    for i in range(1,20):
        if i//2==0:
            f.write(str)
#-------------------------------------------------------------------#
#I I I I I I I#
#V V V V V V V#

#I-----------I# 
#I Főprogram I#
#I-----------I#

#I I I I I I I#
#V V V V V V V#

#feladat1()
#feladat2()
#feladat3()
#feladat4()
#feladat5()
#feladat6()
#feladat7()
feladat8()