import math

hitrost_iztrelka = float(input("Vnesi hitrost iztrelka (m/s): "))
kot = float(input("Vnesi kot(°): "))
s = (hitrost_iztrelka**2*math.sin(math.radians(kot*2)))/9.81

print("Pot, ki jo opravi je: ", s)



