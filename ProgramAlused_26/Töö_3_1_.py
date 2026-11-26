while True:
    print("vali ülesanne:  \n1 \n2 \n3 \n4 \n5")
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
korutis = 1
for i in range(0,8,1):
    arv=float(input(f"{i+1}. arv: "))
    if arv>0:
        korutis*=arv
    print("korutvärtus: ",korutis)

#4
for i in range(10, 21):
    print(f"{i}^2 on {i ** 2}")

#5
try:
    while True:
        N = int(input("Sisesta arv N: "))
        if N > 0: break
    summa = 0
    for i in range(N):
        arv = float(input(f"{i + 1}. arv: "))
        if arv < 0:
            summa += arv
    print("Negatiivsete arvude summa:", summa)

except ValueError:
    print("Palun sisesta kehtiv täisarv.")


    #6
elif valik == '6':
    pos_kogus=0
    neg_kogus=0
    null_kogus=0
    while True:
        try:
            N = int(input("Sisesta arv N > 0:"))
            if N > 0: break
        except ValueError:
            print("Palun sisesta kehtiv täisarv.")
            continue
    for i in range(N):
        while True:
            try:
                arv = float(input(f"{i+1}. arv: "))
                break
            except ValueError:
                print("Palun sisesta kehtiv arv.")
        if arv < 0:
            print("Negativne arv")
            neg_kogus += 1
        elif arv > 0:
            print("Positivne arv")
            pos_kogus += 1
        else:
            print("Null")
            null_kogus += 1
    print(f"Negativsete arvude kogus: {neg_kogus}")
    print(f"Positivsete arvude kogus: {neg_kogus}")
    print(f"Nullide kogus: {neg_kogus}")

        #7

elif valik == '7':
    while True:
        try:
            A = int(input("Sisesta arv A: "))
            B = int(input("Sisesta arv B: "))
            K = int(input("Sisesta arv K: "))
            break
        except ValueError:
            print("Palun sisesta kehtiv täisarv.")
        if A>B:
            print("A peab olema")
    elif valik.lower() == 'q':
        print("Programmist väljumine")
        break
    else:
        print("Viga: Plaun sisesta number (1-5) või 'q' väljumiseks: ")


        

    