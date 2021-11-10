#1. Legyenek adottak a következő listák :
#t1 = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
#t2 = ['Január', 'Február', 'Március', 'Április', 'Május', 'Június', 'Július', 'Augusztus', 
#'Szeptember', 'Október', 'November', 'December']
#Írjon egy kis programot, ami egy új t3 listát hoz létre. Ennek felváltva kell tartalmazni 
#a két lista minden elemet úgy, hogy minden hónap nevét követnie kell a megfelelő 
#napok számának : ['Januar',31,'Februar',28,'Marcius',31, stb...].

'''
t1 = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
t2 = ['Január', 'Február', 'Március', 'Április', 'Május', 'Június', 'Július', 'Augusztus', 'Szeptember', 'Október', 'November', 'December']
t3 = []
cv=0
while cv<12:
    t3.append(t2[cv])
    t3.append(t1[cv])
    cv+=1
#Csúnya:
print(t3)
#Szép:
for item in t3:
    print(item+end=" ")

#               másik megoldás
t4=[]
for i in range(0,12):
    t4.append(t2[1])
    t4.append(t1[i])
for item in t4:
    print(item,end=" ")
'''

#2. Írjon egy programot, ami kiíratja egy lista összes elemét. Ha például a fenti gyakorlat 
#t2 listájára alkalmaznánk, akkor a következőt kellene kapnunk :
#Január Február Március Április Május Június Július Augusztus Szeptember Október November December

'''
list= ['Január', 'Február', 'Március', 'Április', 'Május', 'Június', 'Július', 'Augusztus', 'Szeptember', 'Október', 'November', 'December']
print(list,end=" ")
print()
'''

#3. Írjon egy programot, ami megkeresi egy adott lista legnagyobb elemet. Például, ha a 
#[32, 5, 12, 8, 3, 75, 2, 15], listára alkalmaznánk, akkor a következőt kellene kiírnia : a 
#lista legnagyobb elemének az érteké 75.

'''
list=[32, 5, 12, 8, 3, 75, 2, 15]
print('A lista:', list)
list.sort()
print("A legnagyobb szám:")
print(list[-1])
'''


#4. Írjon egy programot, ami megvizsgálja egy számlista minden elemet (például az előző 
#példa listáját) azért, hogy két új listát hozzon létre. Az egyik csak az eredeti lista páros 
#számait tartalmazza, a másik a páratlanokat. Például, ha a kiindulási lista az előző 
#gyakorlat listája, akkor a programnak egy páros listát kell létrehoznia, ami a [32, 12, 8, 
#2] t tartalmazza es egy páratlan listát ami [5, 3, 75, 15] t tartalmazza. Trükk : 
#Gondoljon az előzőekben említett modulo (%) operátor használatára !

'''
szamok=[32, 5, 12, 8, 3, 75, 2, 15]
paros=[]
paratlan=[]
for item in szamok:
    if item%2==0:
        paros.append(item)
    else:
        paratlan.append(item)
print("Páros számok:", end=" ")
for item in paros:
    print(item, end=" ")
print()
print("Páratlan számok:", end=" ")
for item in paratlan:
    print(item, end=" ")
print()
'''

#5. Írjon egy programot, ami egy szavakból álló lista elemeit egyenkent megvizsgálja
#azért, hogy két új listát hozzon létre. (például: ['Jean', 'Maximilien', 'Brigitte', 'Sonia', 
#'JeanPierre','Sandra'] Az egyikben 6 karakternél rövidebb szavakat legyenek, a 
# másikban 6, vagy annál több karaktert tartalmazó szavak legyenek.

'''
szavak=['Jean', 'Maximilien', 'Brigitte', 'Sonia', 'JeanPierre','Sandra']
hatnalkevesebb=[]
maradek=[]
for item in szavak:
    if len(item)<6:
        hatnalkevesebb.append(item)
    else:
        maradek.append(item)
print('6-nál kevesebb szavak:', end=" ")
for item in hatnalkevesebb:
    print(item, end=" ")
print()
print("6-nál több karakterű szavak")
for item in maradek:
    print(item, end=" ")
print()
'''