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
