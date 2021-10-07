#4. Írj programot, ami beolvas egy számot, majd kiírja a kétszeresét!

"""
a=int(input("Kérek egy számot! a="))
print("A szám kétszerese", 2*a)

a=float(input("Kérek egy számot! a="))
print("A szám kétszerese", 2*a)

----------------------------------------------------------------------------------------------------------------
5. Írj programot, ami beolvas két számot, majd kiírja:
a. az összegüket;
b. különbségüket;
c. szorzatukat;
d. hányadosukat, ha lehet!
e. mennyi maradékot kapunk, ha az első bekért számot osztjuk a másikkal!

a= int(input("Kérek egy egész számot: a - "))
b= int(input("Kérek egy egész számot: b - "))
print("A két szám összege:", a+b)
print(a,'+',b,'=',a+b)

print("A számok szorzata:" , a*b)
print(a, "*" ,b,'=', a*b)

print("A számok különbsége:",a-b)
print(a, "-" ,b, '=', a-b)

print("A számok hányadosai:",a**b)
print(a, '**', b, '=', a**b)

print("A számok maradéka",a%b)
print(a, "%", b,'=', a%b)
----------------------------------------------------------------------------------------------------------------
#8. Írj programot, mely beolvas két egész számot, és kiírja a képernyőre a nagyobbat!

a= int(input("Kérek egy egész számot: a - "))
b= int(input("Kérek egy egész számot: b - "))

if a>b:
    print("'a', nagyobb mint 'b'")
if a<b:
    print("az 'a' kissebb mint 'b'")
if a==b:
    print("a két szám egyenlő")


----------------------------------------------------------------------------------------------------------------

a= int(input("Kérek egy egész számot: a - "))
b= int(input("Kérek egy egész számot: b - "))
if a>b:
    print("'a', nagyobb mint 'b'")
elif b>a:
    print("'a', nagyobb mint 'b'")
else:
    print("a két szám egyenlő")
----------------------------------------------------------------------------------------------------------------
"""
a = int(input("Kérek egy egész számot: a - "))
b = int(input("Kérek egy egész számot: b - "))
if a!=b:
    print("A nagyobb szám:", max(a,b))
else:
    print("A számok egyenlőek")


































