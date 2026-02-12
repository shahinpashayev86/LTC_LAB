## ========================================================================================= ###
## ============================================ Task 1 ===================================== ###
## ========================================================================================= ###
print("\n Task1")
age = int(input("Zehmet olmasa yashinizi qeyd edin: "))

if age >= 18:
    print("ses vere bilersiniz")
else:
    print("ses vermek huququnuz yoxdur")
## ========================================================================================= ###
## ============================================ Task 2 ===================================== ###
## ========================================================================================= ###
print("\n Task2")
en = float(input("Düzbucaqlının enini daxil edin: "))
uzunluq = float(input("Düzbucaqlının uzunlugunu daxil edin: "))

netice = en * uzunluq
print(f"Düzbucaqlının sahəsi: {netice}")
## ========================================================================================= ###
## ============================================ Task 3 ===================================== ###
## ========================================================================================= ###
print("\n Task3")
for i in range(1,10):
    print(i)
## ========================================================================================= ###
## ============================================ Task 4 ===================================== ###
## ========================================================================================= ###
print("\n Task4")
limit = int(input("Limit ədədi daxil edin : "))
cəm = 0

for i in range(limit):
    if i % 2 == 0:
        cəm = cəm + i
print(cəm)
## ========================================================================================= ###
## ============================================ Task 5 ===================================== ###
## ========================================================================================= ###
print("\n Task5")
passwd = "secret123"

while True:
    password = input("Şifrəni daxil edin: ")
    if password == passwd:
        print("Girish ugurludur")
        break
    else:
        print("Yeniden cehd edin")
## ========================================================================================= ###
## ============================================ Task 6 ===================================== ###
## ========================================================================================= ###

print("\n Task6")
import random

gizli_reqem = random.randint(1, 10)
cehd_sayi = 3
print(gizli_reqem)

while cehd_sayi > 0:
    texmini_reqem = int(input("Reqemi daxil edin ( 1-10) : "))
    if texmini_reqem == gizli_reqem:
        print("tebrikler gizli reqemi tapdiz")
        break
    elif texmini_reqem > gizli_reqem:
        print("Daha kicik reqem daxil edin")
    else:
        print("Daha boyuk reqem daxil edin")
    cehd_sayi -= 1
    print("Qalan cehd:", cehd_sayi)

if cehd_sayi == 0 and texmini_reqem != gizli_reqem:
    print("Oyun bitdi. Gizli reqem:", gizli_reqem)

