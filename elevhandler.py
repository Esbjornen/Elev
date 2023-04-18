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

    def add_elev(self, elevnamn, utbildning, tel):
        t_elev = elev.Elev(elevnamn, utbildning, tel)
        self.elevlist.append(t_elev)

    def print_elevlist(self):
        self.elevlist = sorted( self.elevlist, key=lambda p: p.namn )     

        print ("\n-------------------------------------")    
        print("-LstarElever-")

        for elev in self.elevlist:
            print(elev.get_elev())

    def del_elev(self):
        print("\nTa bort elev--------------------------")

        tel = input("Mata in tel för elev som ska tas bort: ")

        try:
            self.elevlist = [p for p in self.elevlist if p.tel != tel]

        except ValueError:
            print("\n kunde inte ta bort eleven")    