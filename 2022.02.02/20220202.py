
def feladat17():
    szo=input("Adj meg egy szót! : ")
    print("A szó ennyi karakterből áll:", len(szo))

#-------------------------------------------------------------------------
def feladat18():
    szo=input("Adj meg egy szót!:")   
    e= 0
    for item in szo:
        if item=='e':
            e+=1
    print("Az addot szó:", szo, ", ennyi e betüből áll:", e)
    #Vagy szo.count("e")
#-------------------------------------------------------------------------
def feladat19():
    szo=input("Kérek egy szót:")
    maganhangzok= 'aáeéiíoóüűöőuúAÁOÓÖŐUÚŰÜEÉ'
    mh= 0
    for item in szo:
        if item in maganhangzok:
            mh+=1
    print("A szóban lévő magánhangzók száma:", mh)
#-------------------------------------------------------------------------
def feladat20():
    mondat= input("Kérek egy mondatot: ")
    print("A szó ennyi karakterből áll:", len(mondat))
#-------------------------------------------------------------------------
def feladat21():
    mondat=input("Kérek egy mondatot!:")
    space= 0
    for item in mondat:
        if item== " ":
            space+=1
    print("A mondatban ennyi space található", space)
#-------------------------------------------------------------------------
def feladat22():
    mondat=input("Kérek egy mondatot!: ")
    eszam= 0
    for item in mondat:
        for item== "e":
            eszam+=1
    print("Ennyi e betű található a mondatban:", eszam)
#-------------------------------------------------------------------------
def feladat23():
    mondat=input("Adj meg egy mondatot!:")
    szoszam= 1
    for item in mondat:
        if item== " ":
            szoszam+=1
    print("A mondat ennyi szóból áll:", szoszam)
#-------------------------------------------------------------------------
def feladat24():
    mondat=input("Kérek egy mondatot!:")
    szavak= mondat.split(' ')
    print(len(szavak))
    for item in szavak:
        print(item, "hossza", len(item))

#-------------------------------------------------------------------------
def feladat26():
    mondat=input("Kérek egy mondatot!:")
    mondatszam= 0
    for item in mondat:
        if item== "!.?":
            mondatszam+=1
    print("A mondatok száma:", mondatszam)
#-------------------------------------------------------------------------
#_____________________#
#I    Fő porgram     I#
#_____________________#
#feladat17()
#feladat18()
#feladat19()
#feladat20()
#feladat21()
#feladat22()
#feladat23()
#feladat24()
#feladat26()
