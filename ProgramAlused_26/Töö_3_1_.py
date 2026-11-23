while True:
    print("vali ülesanne:  \n1 \n 2 \n 3 \n 4 \n 5")
    valik=input("Sisesta ülesande number (1-5) või 'q' väljumiseks:  ")
# Ül. 1

from multiprocessing.reduction import DupFd
from os import fsdecode
from turtle import fd


i = 0
kogus = 0
while i < 15:
    arv = float(input(f"{i + 1}. arv: "))
    if arv.is_integer():
        kogus += 1
    i += 1
print("Täisarve:", kogus)

# 2
try:
    while True:
    A=int(input("Sisesta arv A: "))
    if A > 0:
        summa = 0
        for i in range(1, A + 1):
            summa += i
        print("Summa:", summa)
        break
    else:
        print("Palun sisesta positivne täisarv.")
except ValueError:
    print("Palun sisesta kehtiv täisarv")

# 3
i = 0
korutis = 1
while i<8:
    arv=int(input(f"{i+1}. arv: "))
    if arv>0:
        korutis*=arv
    i+=1
    print("korutvärtus: ",korutis)

4
for i in range(10, 21):
    print(f"{i}^2 on {i ** 2}")

5
try:
    while True:
        N = int(input("Sisesta arv N: "))
        if N > 0:
    summa = 0
    for i in range(N):
        arv = float(input(f"{i + 1}. arv: "))
        if arv < 0:
            summa += arv
    print("Negatiivsete arvude summa:", summa)

except ValueError:
    print("Palun sisesta kehtiv täisarv.")

    