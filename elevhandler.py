import elev

class ElevHandler:

    #Konstruktor-----------------------------------
    def __init__(self):
        self.elevlist = []

    def print_meny(self):
        print("------------------------")
        print("\n\tMENY\n")
        print("\t1. Lista elever")
        print("\t2. Lägg till elev")
        print("\t3. Ta bort elev")
        print("\t4. Spara och Avsluta")

        val = input("Gör ett val: ")

        return val