eesnimi=input("Siseta eesnimi: ")
if eesnimi.upper()=="JUKU":
    print("Läheme Jukuga Kinno!")
    if eesnimi.isupper():
        print("Ära karju, Juku!")
    elif eesnimi.islower():
        print("Ära sosista, Juku!")

    try:
        vanus=int(input("Kui vana sa oled, Juku?"))
        if 0 <=vanus < 6:
            pilet="tastapilet"
        elif 6 <= vanus <=14:
            pilet="lapsepilet"
        elif 15 < vanus < 65:
            pilet="täispilet"
        elif 65<=vanus<100:
            pilet="soodusilet"
        else:
            print("Viga ndmetes.")
        try:
            print(f"Juku vanus on {vanus} aastat, seega on vaja osta {pilet}.")
        except NameError:
            print("Piletit ei saa määrata, kuna vanus on vale. ")
    except ValueError:
        print("Palun sisesta oma vanus nimbrina.")
else:
    print("Täna kinno ei minda.")

    #Klasiitöö 16.11.2026
pinginaabrid=["Anna","Vika"]
nimi1=input("Sisesta esimese inimise nimi: ")
nimi2=input("Sisesta teise inimese nimi: ")
if nimi1.isalpha() and nimi2.isalpha():
    if nimi1.capitalize() in pinginaabrid nimi2.capitalize() in pinginaabrid:
        print(f"{nimi1} ja {nimi2} on täna pinginaabrid.")
    else:
        print(f"{nimi1} ja {nimi2 ei ole täna pinginaabrid.")
