from gc import DEBUG_SAVEALL


pinginaabrid=["Anna","Vika"]
nimi1=input("Sisesta esimese inimise nimi: ")
nimi2=input("Sisesta teise inimese nimi: ")
if nimi1.isalpha() and nimi2.isalpha():
    if nimi1.capitalize() in pinginaabrid and nimi2.capitalize() in pinginaabrid:
        print(f"{nimi1} ja {nimi2} on täna pinginaabrid.")
    else:
        print(f"{nimi1} ja {nimi2} ei ole täna pinginaabrid.")
else:
    print("Viga: nimed peavad koosnema ainult tähtedest.")
#otsing nimede algustähtede järgi
valik=input("Kas soovid otsida nimede alhustähtede järgi? (jah/ei): ").lower()
if valik=="jah":
    algustäht=input("Sisesta algustäht: ").capitalize()
    for nimi in pinginaabrid:
        if nimi.startswith(algustäht):
            print(f"{nimi} algab tähenda {algustäht}.")
else:
    print("Otsingut ei tehta.")

    # 3. Remont
try:
    pikkus=float(input("Sisesta toa pikkus meetriteas: "))
    laius=float(input("Sisesta toa laius meetrites: "))
    pindala=pikkus*laius
    print(f"Toa põranda pindala on {pindala} ruutmetrit")
    valik=input("Kas soovid remonti teha? (jah/ei): ").lower()
    if valik=="jah":
        try:
            rm_hind=float(input("Sisesta ruutmeetri hind: "))
            hind=round(pindala*rm_hind,2)
            print(f"Põranda vahetamise hind on {hind} eurot.")
            valik=input("Kas tahad remonti teha ise? (jah/ei): ").lower()
            if valik=="jah":
                print(f"Remonti teed ise, koguhind on {hind} eurot.")
            elif valik=="ei":
                try:
                    töö_hind=float(input("Sisesta töö hind ruutmeetri kohta: "))
                    hind=round(hind+pindala*töö_hind,2)
                    print(f"Remonti teeb professional, koguhind on {hind} eurot.")
                except ValueError:
                    print(f"Viga: Palun sisesta numbriline väärtu töö hinna jaoks.")
            else:
                print("Viga: Palun sisesta jaj või ei.")
        except ValueError:
            print("Viga: Palun sisesta numbriline väärtus ruutmeetri hinna jaoks.")
    else:
        print("remonti ei tehta.")
except ValueError:
    print("Viga: Palun sisesta numbrilised väärtused pikkuse ja laiuse jaoks.")

    # 4. Allahindlus
hind = float(input("Sisesta toote hind: "))
if hind > 700:
    hind = hind * 0.7
print(f"Lõplik hind: {hind:.2f} €")
    
    # 5. Temperatuur
try:
    temp = float(input("Sisesta toatemperatuur: "))
    if temp > 18:
        print("Temperatuur on üle 18 kraadi.")
    else:
        print("Temperatuur ei ole üle 18 kraadi.")
except ValueError:
    print("Viga! Sisesta arv.")

    # 6. Pikkus
# Piirid:
# lühike – alla 160 cm
# keskmine – 160 kuni 180 cm
# pikk – üle 180 cm
pikkus = float(input("Sisesta oma pikkus (cm): "))
if pikkus < 160:
    print("Sa oled lühike.")
elif pikkus <= 180:
    print("Sa oled keskmise pikkusega.")
else:
    print("Sa oled pikk.")

    # 7. Pikkus ja sugu


    # 8. Poes
summa=0
arve="Toode  Kogus  Hind  Kokku"
valik=input("Kas soovid osta piima? (jah/ei): ")
if valik.lower()=="jah"
    kogus=input("Kui plaju piima soovid osta (täisarv): ")
    if kogus.isdigit():
        kogus=int(kogus)
        piim_hind=round(uniform(o.5, 3), 2)
        print(f"Piima hind on {piim_hind} eurot.")
        summa+=kogus*piim_hind
        print(f"Piima kogusmma on {kogus*piim_hind} eurot.")
        arve=f"piim     {kogus}     {piim_hind}     {kogus*piim_hind}"
else:
    print("Selge: Piima ei taha")
print(f"Kogusimma om: {round(summa,2)} eurot")


valik=input("Kas soovd osta sai? (jah/ei): ")


print("\n----- TŠEKK -----")
print(tsekk)
print(f"KOKKU: {summa_kokku:.2f} €")

    #9
a = float(input("Sisesta 1. külg: "))
b = float(input("Sisesta 2. külg: "))
c = float(input("Sisesta 3. külg: "))
d = float(input("Sisesta 4. külg: "))

if a <= 0 or b <= 0 or c <= 0 or d <= 0:
    print("Viga! Kõik küljed peavad olema positiivsed.")
elif a == b == c == d:
    print("See nelinurk võib olla ruut.")
else:
    print("See nelinurk ei ole ruut.")
