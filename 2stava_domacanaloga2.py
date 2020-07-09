from random import *

st_kovancev = 10

while st_kovancev > 0:
    kocka = randrange(1,6)
    stava = int(input("stava? "))
    if stava > st_kovancev:
        print("GOLJUF, ZA KAZEN TI UZAMEM 1 KOVANEC")
        st_kovancev = st_kovancev - 1
    elif kocka % 2 == 0:
        print("Kocka je padla na: ", kocka)
        st_kovancev = st_kovancev + stava
        print("Dobil stavo, imaš", st_kovancev)
    elif kocka % 2 == 1:
        print("Kocka je padla na :", kocka)
        st_kovancev = st_kovancev - stava
        print("Izgubil stavo, imaš", st_kovancev)
print("Konec igre")


