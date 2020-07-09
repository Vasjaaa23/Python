from random import *

karte = list(range(1, 7)) * 2
shuffle(karte)
peter, pavel = karte[:6], karte[6:]

print("Peter v začetku: ", peter)
print("Pavel v začetku: ", pavel)
print()

novi_peter = []
novi_pavel = []

for i,j in zip(peter,pavel):
    if i > j:
        novi_peter.append(i)
        novi_peter.append(j)

    elif j > i:
        novi_pavel.append(j)
        novi_pavel.append(i)


print("Peter na koncu: ",novi_peter)
print("Pavel na koncu: ",novi_pavel)






