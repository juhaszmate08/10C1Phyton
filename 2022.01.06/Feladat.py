from math import *

def projekt():
    #Listák
    havikereset=[int(input("Mennyi a havi kereset?(írj be egy összeget):" ))]
    rezsi=[int(int("Mennyi a havi rezsi költség?: "))]
    pluszkoltseg=[int(input("Mennyi a havi plussz költség?:"))]
    sporolas=[]
    maradek=[]

    #Szöveg rész
    print("Milyen háztartási árakat kell beszámolni, beleszámítani a költségvetésekbe?!")
    print()
    print("Rezsi, Alap szükségletek, Plussz költségvetések, Spórolások, megmaradt pénz")
    print()
    print("A havi keresetnek megadott összeg:", havikereset ,"Ft")
    print()
    print("A havi rezsinek megadott összeg:", rezsi, "Ft")
    print()
    print("A havi plusszköltségnek megadott összeg:", pluszkoltseg, "Ft")
    print()

    #Az alprogram
    print(rezsi + pluszkoltseg)



#Főprogram
projekt()