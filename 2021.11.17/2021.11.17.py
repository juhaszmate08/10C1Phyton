'''
2. Tróbálja megírni a megtalal() függvényt, ami az ellenkezőjét csinálja, mint amit az 
indexoperátor (vagyis a []) tesz. Ahelyett, hogy egy megadott indexhez megtalálja az annak 
megfelelő karaktert, ennek a függvénynek egy adott karakterhez tartozó indexet kell 
megtalálni.
Máshogyan fogalmazva, egy olyan függvényt kell írni, ami két argumentumot vár : a 
kezelendő karakterlánc nevét és a keresendő karaktert. A függvénynek visszatérési értékként 
az első ilyen karakter stringbeli indexét kell megadni a karakterláncban. Így például : print 
megtalal("Juliette &Roméo", "&") eredménye : 9
Figyelem : Gondolni kell minden lehetséges esetre. Arra is számítanunk kell, hogy a függvény
visszatérési értékként egy speciális értéket (például -1et) ad, ha a keresett karakter nincs a
karakterláncban.
'''

def megtalal(szoveg,karakter,kezdoindex):
    ujszoveg=szoveg[kezdoindex:]
    if karakter in szoveg:
        return ujszoveg.index(karakter)
    else:
        return -1
#feladat2
def feladat2():
    akarmi='Lorem ipsum dolor sit amet, consectetur adipisicing elit. Quis odio soluta illum aliquid, deleniti reprehenderit, doloremque ut mollitia perferendis, molestias dolore dolores delectus? Cupiditate necessitatibus, consequatur maiores omnis nostrum eveniet incidunt ipsum placeat. Neque nobis molestiae dolores nisi, at, minus mollitia doloribus dolor, blanditiis eos minima aperiam necessitatibus perferendis suscipit.'
    kar='i'
    # kiírás:
    print(megtalal(akarmi, kar,10))
    #változóba tesszük a visszaküldött értéket
    kapottindex=megtalal(akarmi,kar,10)
    print(kapottindex)
    if kapottindex>-1:
        print("A megadott karakter a szövegben először", str(kapottindex)+ '. indexű helyen fordul elő')
    else:
        print('A megadott karakter nem található a szövegben!')

def karakterszam(szoveg, karakter):
    return szoveg.count(karakter)

#feladat4
def feladat4():
    akarmi='Lorem ipsum dolor sit amet, consectetur adipisicing elit. Quis odio soluta illum aliquid, deleniti reprehenderit, doloremque ut mollitia perferendis, molestias dolore dolores delectus? Cupiditate necessitatibus, consequatur maiores omnis nostrum eveniet incidunt ipsum placeat. Neque nobis molestiae dolores nisi, at, minus mollitia doloribus dolor, blanditiis eos minima aperiam necessitatibus perferendis suscipit.'
    kar="i"
    print("A megadott szövegben a megadott karakter", karakterszam(akarmi, kar),'alkalommal szerepel')

#feladat5
def feladat5():
    prefixes='JKLMNOPQ'
    suffixe='ack'
    nevek=[]
    for item in prefixes:
        nevek.append(item+suffixe)
        for item in nevek:
            print(item, end=" ")

#feladat6
def feladat6():
    mondat='Lorem ipsum dolor sit amet, consectetur adipisicing elit. Quis odio soluta illum aliquid, deleniti reprehenderit, doloremque ut mollitia perferendis, molestias dolore dolores delectus?'
    print('A mondat', karakterszam(mondat,' ')+1,'szóból áll')








#feladat2()
#feladat4()
#feladat5()
feladat6()









