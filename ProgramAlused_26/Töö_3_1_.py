import random
while True:
    print("""
          1. Täisarvude loendamine
          2. Naturaalarvude summa
          3. Positiivsete arvude korrutis
          4. Arvude ruudud
          5. Negatiivsete arvude summa
          6.Klaviatuurilt sisestatakse N arvu.
            Koosta programm, mis määrab sisestatud arvude seast:
            negatiivsete arvude arvu,
            positiivsete arvude arvu,
            nullide arvu.(N väärtus sisestatakse klaviatuurilt.)
          7. Väljastada ekraanile arvud, mis on K-ga jaguvad vahemikust [A, B].""")
    valik=input("Sisesta ülesande number (1-31) või 'q' väljumiseks: ")
# Ül. 1

    if valik == '1':
        i = 0  # loendur
        kogus = 0  # täisarvude kogus
        while i < 15:
            arv = float(input(f"{i + 1}. arv: "))
            if arv.is_integer():
                kogus += 1
            i += 1
        print("Täisarve:", kogus)

# 2
    elif valik == '2':
        i = 0  # loendur
        kogus = 0  # naturaalarvude summa
        while i < 15:
            arv = float(input(f"{i + 1}. arv: "))
            if arv.is_integer() and arv > 0:
                kogus += arv
            i += 1
        print("Naturaalarvude summa:", kogus)

# 3
    elif valik == '3':
        korutis = 1
        for i in range(0,8,1):
            arv=float(input(f"{i+1}. arv: "))
            if arv>0:
                korutis*=arv
            print("korutvärtus: ",korutis)

#4
    elif valik == '4':
        for i in range(10, 21):
            print(f"{i}^2 on {i ** 2}")

#5
    elif valik == '5':
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
                K = int(input("Sisesta arv K: "))#Tee K kontroll, et see ei oleks 0
                break
            except ValueError:
                print("Palun sisesta kehtiv täisarv.")
            if A>B:
                print("A peab olema väiksem või võrdne B-ga. Siis vahetame need.")
                A,B=B,A
        print(f"Arvud vahemikus [{A}, {B}], mis on {K}-ga jaguvad:")
        for i in range(A, B + 1):
            if i % K == 0:
                print(i)
    
#Iseseisev töö:

# 12
    elif valik == '12':
        n = int(input("Niidukite arv N: "))
        m = float(input("Esimese niiduki tööaeg m (tundides): "))

        kokku = 0
        aeg = m
        for i in range(n):
            kokku += aeg
            aeg += 10 / 60  # 10 minutit tundides
        print(f"Brigaad töötas kokku {kokku:.2f} tundi")
    

# 17
    elif valik == '17':
        arv = int(input("Sisesta arv: "))

        for i in range(1, 10):
            print(f"{arv}*{i}={arv * i}")
    

# 22
    elif valik == '22':
        summa = 0
        for i in range(100, 201):
            if i % 17 == 0:
                summa += i

        print("17-ga jaguvate arvude summa:", summa)

#28
    elif valik =='28':
        salajane = random.randint(1, 100)
    katsed = 0
    print("Arvasin ühe arvu vahemikus 1 kuni 100. Arva ära!")

    while True:
        pakkumine = int(input("Sinu pakkumine: "))
        katsed += 1
        if pakkumine < salajane:
            print("Minu arv on suurem")
        elif pakkumine > salajane:
            print("Minu arv on väiksem")
        else:
            print("Õige! Arvasid ära.")
            break

    print("Katsete arv:", katsed)
    

#31
    elif valik == '31':
        k = int(input("Kotlettide arv K: "))
        m = int(input("Mitu kotletti mahub pannile M: "))
        
        pannid= 0
        while True:
            if k < m:
                break
            k -= m
            pannid += 1
    elif valik.lower() == 'q':
        print("Programmist väljumine")
        break
    else:
        print("Viga: Plaun sisesta number (1-31) või 'q' väljumiseks: ")


    