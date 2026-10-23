from random import *    #randint
print("Tere, maailm!")
nimi=input("Sisesta oma nimi: ")
print(f"Tere, maailm! Tervitan sind {nimi}!")
try:
    vanus=int(input("Sisesta oma vanus: "))
    print(f"Tere, maailm! Tervitan sind {nimi}! Sa oled {vanus} aastat vana.")
except ValueError:
    print("Palun sissesta kehtiv number vanuse jaoks.")

    #Ülesanne 3
vanus=18 #int-täisarv
eesnimi="Jaak" #str-sõne
pikkus=16.5 #float-kümnendmurd/ujukomaarv
kas_käib_koolis=True #bool-tõeväärtus
print(f"Vanus:{vanus}, tüüp:{type(vanus)}")
print(f"Eesnimi:{eesnimi}, tüüp:{type(eesnimi)}")
print(f"Pikkus:{pikkus}, tüüp:{type(pikkus)}")
print(f"Käib koolis:{kas-käib_koolis}, tüüp:{type(kas-käib_koolis)}")

from random import *    #randint
kommide_arv=randint(1, 100)                                              #(input("kommide arv: "))
print(f"Laud on {kommide_arv} kommi.")
kommid=int(input("Mitu kommi soovid ära võtta?. "))
kommide_arv -= kommid
print(f"Laud on nüüd {kommide_arv} kommi. ")
