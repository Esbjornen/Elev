import elevhandler


looping = True

skola = elevhandler.ElevHandler()



while looping:
    val = skola.print_meny()

    if (val == "1"):
        print("\nlista elever\n")
        skola.print_elevlist()
        input("\n\ntryck enter för att fortsätta!\n\n")

    elif (val == "2"):
        print("\nLägg till Elev\n")
        namn = input("Mata in namntet: ")
        utb = input ("Mata in utbilding: ")
        tel = input ("Mata in telefonnummer")

        skola.add_elev(namn, utb, tel)


    
    elif (val == "3"):
        skola.del_elev()

    

    elif (val == "4"):
        break