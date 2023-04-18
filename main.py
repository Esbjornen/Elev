import elevhandler


looping = True

skola = elevhandler.ElevHandler()



while looping:
    val = skola.print_meny()

    if (val == "1"):
        print("\nlista elever\n")

    elif (val == "2"):
        print("\nadd elev\n")

    elif (val == "3"):
        print("\nremove elev\n")

    elif (val == "4"):
        break