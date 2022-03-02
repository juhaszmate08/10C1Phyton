def bevezeto():
    listanév=[]
    #Az elemeit indexeljük, fontos hogy 0-tól kezdődik az indexelés!
    #elemek hozzáadása= lista.append(érték)
    #listanév[0]="alma" listanév[1]=12.3
    #listanév=[érték1,érték2,érték3]
    #Tetszőleges tipusú adatokat tárolhat

    #Szám típus:
    #sum(), min(), max() stb...
#--------------------------------------#
def feladat1():
    #első 20 négyzetszám
    negyzetszamok=["alma", "körte"]
    for i in range(1,21):
        negyzetszamok.append(pow(i,2))
    print(negyzetszamok)
    for item in negyzetszamok:
        print(item, end=" ")
#--------------------------------------#
def feladat2():
    harmasszorzo=[]
    for i in range(1,31):
        harmasszorzo.append(i*3)
    for item in harmasszorzo:
        print(item, end=" ")
    print()
    print(len(harmasszorzo))
    print(sum(harmasszorzo))
    print(min(harmasszorzo))
    print(max(harmasszorzo))
#--------------------------------------#
#------------------------#
#Itt kezdődik a Főprogram!
#------------------------#
#bevezeto()
#feladat1()
feladat2()
