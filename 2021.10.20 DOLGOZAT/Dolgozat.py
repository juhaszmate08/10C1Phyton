# 1. kész
a= int(input("Kérek egy valós számot: "))
print("A szám háromszorosa:",a*3)
print("--------------------")
#------------------------------------------------------------------
#2 kész
h= int(input("Add meg a háromszög egyik oldalát(cm): "))
j= int(input("A háromszög magassága(cm):"))
print("A háromszög területe:", h+j%2, "cm" )
#------------------------------------------------------------------
#3 kész
b= int(input("Kérek egy egész számot: "))
if b%5==0:
    print("A(z)", b, "szám oszható öttel")
else:
    print("a" ,b, "nem osztható 5-el.")

#------------------------------------------------------------------
#4 NEM MŰKÖDIK
'''c= int(input("Kérek egy egész számot: "))
if:
for i in range(-50,21):
        print("a szám -50 és 21 között található meg."):
print("--------------------")'''
#------------------------------------------------------------------
#5 kész
for i in range(0,21,2):
    print(i, end=" ")
print()
#------------------------------------------------------------------
#6
for i in range(1,21):
    if i%3==2:
        print(i, end=" ")
print()
#------------------------------------------------------------------
#7 kész
for i in range(1,126):
    if i%4==0:
        print(i)
print()
#------------------------------------------------------------------