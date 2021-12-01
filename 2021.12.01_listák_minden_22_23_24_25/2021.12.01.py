     #                                                                                  23-23-24-25 FELADATOK


     #Írjon egy scriptet, ami a 2, 3, 5, 7, 11, 13, 17, 19 es szorzótáblák első 15 tagját állítják elő a 
     #képernyőn a következő táblázathoz hasonlóan (ezeket a számokat egy listába fogjuk elhelyezni):
     #2 4 6 8 10 12 14 16 18 20 22 24 26 28 30
     #3 6 9 12 15 18 21 24 27 30 33 36 39 42 45
     #5 10 15 20 25 30 35 40 45 50 55 60 65 70 75

'''
     szamok=[2, 3, 5, 7, 11, 13, 17, 19]
     for item in szamok:
          for i in range(1,16):
               szamok.append(item*1)
          print()
          print(szamok)
          szamok.clear()
'''
     #főprogram itt kezdődik




#Legyen adott a következő lista :
#['JeanMichel', 'Marc', 'Vanessa', 'Anne', 'Maximilien', 'AlexandreBenoît', 'Louise']
 #Írjon egy scriptet, ami kiírja a neveket és a nevekben lévő karakterek számát.                    [MŰKÖDIK]
'''
     nevek=['JeanMichel', 'Marc', 'Vanessa', 'Anne', 'Maximilien', 'AlexandreBenoît', 'Louise']
     for item in nevek:
          print(item, len(item))
'''



#Van egy egész számokat tartalmazó lista, amiben egyes számok többször is előfordulnak. 
#Írjon egy scriptet, ami a listát úgy másolja át egy másik listába, hogy figyelmen kívül hagyja a 
#többszöri előfordulásokat. A végső listának rendezettnek kell lenni.
'''
     szamok = [31,28,31,30,31,30,31,31,30,31,30,31]
     ujlista=[]
     for item in szamok:
          if item not in ujlista:
               ujlista.append(item)
          print(ujlista)
'''

#Írjon egy scriptet, ami megkeresi egy adott mondatban a leghosszabb szót (a program 
#felhasználójának be kell tudnia írni egy általa választott mondatot)
'''
mondat=input("Kérek egy mondatot! " )
szavak=mondat.split(' ')
hosszok=[]
print(szavak)
for item in szavak:
     hosszok.append(len(item))
leghosszabb=max(hosszok)
indexe=hosszok.index(leghosszabb)
print(indexe)
print("A leghosszabb szó", szavak[indexe])
'''

#írjon egy programot amely eldönti a megadott számokról hogy páros vagy nem szam=[11,12,15,67,15,35,45,67,89]
szam=[11, 12, 15, 67, 15, 35, 45, 67, 89]
paros=[]
paratlan=[]
print("A megadott számok:", szam)
for item in szam:
     if item%2==0:
          item.append(paros)
          print("páros számok:", paros)
     else:
          item.append(paratlan)
          print("Páratlan számok:", paratlan)
print()







