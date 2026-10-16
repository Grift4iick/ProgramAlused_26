print("Hello, \World!")
print("Tere tulemast\t!")
print("Õpin",1,".kursusel") #sep=" " vaikimisi on tühik
print("Õpin",1,".kursusel",sep="***") #sep="" tähendab et tühikut ei ole



#Parametrid sep ja end
print() #See on tühi rida
print("Õpin",1,".kursusel",sep="***") #sep="" tähendab et tühikut ei ole
print("2026", "10", "01", sep="/")
print("Sama ", end="") #tähendab, et reavahetust ei ole end="\n"
print("rida")


#Mutujad
nimi = "Python" #str ehk sõne
print("Tere,", nimi)
kursus=1
print("Õpin",kursus,".kursusel")


#input funktsioon
nimi = input("Sisesta oma nimi:  ") #programm küsib ja ootab kasutaja sisestust
print("Tere,", nimi)
kursus=int(input("Sisesta oma kursuse numper:  "))
print("Õpin",kursus,".kursusel")
print("Jargmisel aastal õpin ",kursus+1,".kursusel")
#kursus+1 tähendab, et kursuse number 1 võrra")


#liitmine
a = float(input("Esimene arv: "))
b = float(input("Teine arv: "))
print(a,"+",b,"=",a + b)

#astendamine
a = float(input("Esimene arv: "))
b = float(input("Teine arv: "))
print(a,"**",b,"=",a ** b)

#korrutamine
a = float(input("Esimene arv: "))
b = float(input("Teine arv: "))
print(a,"*",b,"=",a * b)

#jagamine
a = float(input("Esimene arv: "))
b = float(input("Teine arv: "))
print(a,"/",b,"=",a / b)
print("Ümardatud arv:",round(a / b,2))

#jagamise täisarvuline osa
a = float(input("Esimene arv: "))
b = float(input("Teine arv: "))
print(a,"//",b,"=",a // b)

#jagamisjääk
a = float(input("Esimene arv: "))
b = float(input("Teine arv: "))
print(a,"%",b,"=",a % b)

print("lahutamine")
a = float(input("Esimene arv: "))
b = float(input("Teine arv: "))
print(a,"-",b,"=",a - b)


#f-sõne formatimine
nimi = "Mari"
punktid = 87
print(f"{nimi} sai {punktid} punkti.")

a =float(input("Esimine arv: "))
tehe=input("Tehe: ")
b =float(input("Teine arv: "))

print(f"{a} {tehe} {b} = {eval(f'{a} {tehe} {b}')}")


import math

print("Pii väärtus:", math.pi)
print("√16 =", math.sqrt(16))
print("sin(π/2) =", math.sin(math.pi / 2))
print("sin(30°) =", round(math.sin(math.radians(30)), 2))
print("5! =", math.factorial(5))d