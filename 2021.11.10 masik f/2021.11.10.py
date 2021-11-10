#                                               (1.) Feladat (phyton)
'''
szo="elkelkáposztástalaníthatatlanságoskodásaitokért"
print('A szó hossza:', len(szo))
darabok=[]
for i in range(0,len(szo),5):
    if i+5<len(szo):
        darabok.append(szo[i:i+5])
    else:
        darabok.append(szo[i:])
print(darabok)
darabok.reverse()
for item in darabok:
    print(item,end="")
'''
#                                               (2.) Feladat (phyton)

def feladat6_2(szoveg, karakter):
    if karakterin szoveg:
        ind=szoveg.index(karakter)
        return ind
    else:
        return -1

szov="Juliette & Romeó"
kar='&'
if feladat6_2(szov, kar)!=-1:
    print("A", kar, "benne van a", szov,"-ban/ben")
else:
    print("A", kar, "nincs benne", szov,"-ban/ben")
feladat6_2(szov, kar)










