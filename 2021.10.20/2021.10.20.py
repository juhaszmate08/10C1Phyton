#                                HÁZI FELADAT
#41. Generálj 10 véletlenszámot és írasd ki a képernyőre vesszővel elválasztva! 

#42. Generálj 20 véletlenszámot 0 és 20 között, és írasd ki a képernyőre vesszővel elválasztva! 

#43. Generálj 15 véletlenszámot 25 és 50 között, és írasd ki a képernyőre vesszővel 
#elválasztva! 

#44. Generálj két egész véletlen számot 10 és 50 között, írasd ki a szorzatát! 


#-------------------------------------------------------------------------------------------


#45. Generálj két véletlen, valós számot 18 és 69 között, írasd ki a hányadukat úgy, hogy a 
#nagyobbat osztod a kisebbel. 
from random import *
def feladat45():
    a=randint(18,69)
    print("a=" ,a)
    b=randint(18,69)
    print("b=" ,b)
    nagyobb=max(a,b)
    kissebb=min(a,b)
    print("Hányaduk:", nagyobb/kissebb)
    print("Hányadosuk:", nagyobb//kissebb)
feladat45()
#46. Generálj 7 véletlen számot, add össze őket és írasd ki a végeredményt! 

#47. Generálj 10db páros számot, szorozd össze őket. Minden szorzatot írass ki!
def feladat47():
     szorzat=1
     cv=1
     while cv<=10:
         gen=randint(1,10)
         if gen%2==0:
             szorzat*=gen
             print(gen,"-", szorzat)
             cv+=1
feladat47()
#48. Generálj számokat 10 és 50 között, amíg a generált érték 25 nem lesz! A generált 
#számokat írd ki egymás mellé (…, …, …, …….25)!
def feladat48():
    gen=randint(10,50)
    print(gen, end=" ")
    while gen !=25:
        gen=randint(10,50)
        print(gen, end="")
print()
feladat48()
#49. A 'keresztül-kasul' szóból véletlenszerűen válasz ki 5 elemet(betűt),fűzd össze őket és 
#írasd ki a végeredményt!