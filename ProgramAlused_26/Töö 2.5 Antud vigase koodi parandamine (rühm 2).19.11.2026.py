#Kontroltöö

try:
    print("Vali programm: \n 1 - Arvu kontroll \n 2 - Kehamassiindeks \n 3 - Ostu allahindlus")
    valik=int(input("Sisesta valik (1-3) =>  "))
    if valik == 1:
        print("Arvu kontroll")  # oli ' => "
        try:
            arv=int(input("Sisesta täisarv => ")) #oli arv=(input("Sisesta täisarv => ")  praegu  arv=int(input("Sisesta täisarv => "))
            if arv>0:                           # oli if arv>0 => if arv>0:
                print("Arv on positiivne") 
            elif arv == 0:                      # oli else if arv=0:  praegu  elif arv == 0:
                print("Arv on null")
            else:
                print("Arv on negatiivne")          # Lisa tab
            if arv%2==0:
                print("Arv on paarisarv")
            else:
                print("Arv on paaritu")
        except ValueError:
            print("Viga")
    elif valik == 2:
        print()
        print("Kehamassiindeks")
        try:
            mass=float(input("Sisesta kaal (kg) => "))
            pikkus=float(input("Sisesta pikkus (m) => "))  # oli pikkus=float(input("Sisesta pikkus (m) => ")  praegu  pikkus=float(input("Sisesta pikkus (m) => "))
            kmi=mass/pikkus**2                              # oli kmi=mass/pikkus*2  praegu  kmi=mass/pikkus**2 
            print("KMI:", round(kmi,1))
            if kmi<18.5:
                print("Alakaal")
            elif kmi < 18.5:                                # oli >=  praegu <
                print("Normaalkaal")
            elif kmi > 25:                                  # oli >=  praegu <
                print("Ülekaal")
            elif kmi > 30:                                  # oli >=; 30  praegu > ; 30:
                print("Rasvumine")
            else:
                print("Viga andmeds")
        except ValueError:
            print("Viga")
    elif valik == 3:
        print()
        print("Ostu allahindlus")
        summa=float(input("Sisesta ostusumma => "))
        if summa <= 0:                                  # oli >=  praegu  <=
            print("Vigane summa")
        elif summa > 500:                   # oli elif summa>100 or summa<=500:  praegu  elif summa > 500:
            print("Allahindlus 10%, maksta:", round(summa*0.9,2))  #oli 
        elif summa > 100:                                            # oli elif summa>500: praegu  elif summa > 100:
            print("Allahindlus 5%, maksta:", round(summa * 0.95, 2))  
        else:                                                          # oli else praegu else:
            print("Allahindlust pole, maksta:", round(summa,2))                 #oli print("Allahindlust pole, maksta:", summa  praegu  print("Allahindlust pole, maksta:", round(summa,2))
    else:
        print("Palun sisesta 1-3 numbrid")
except ValueError:
    print("Palun sisesta number")
    #tööta vigade kallal

        # 1 ülesanne:
    #Parndasin rida 30 oli < praegu >  ja rida 32 oli < praegu >

    #Lisaülesanne:

    #Lisasin programmi algusesse funktsiooni if...elif...else. Kirjutasin ka ridadele 21 ja 41 "select function".
    # Lisasin järgmiste programmide algusesse funktsiooni elif, kuna mul on vaja, et vastav programm käivitataks pärast seda, kui kasutaja on numbri valinud.
    #  Lisasin ka muutuja "val", et kasutaja saaks numbri valida.