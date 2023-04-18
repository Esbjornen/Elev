import elev
import pickle
import os

class ElevHandler:

    #Konstruktor-----------------------------------
    def __init__(self):
        self.elevlist = []
        self.filnamn = "elever.pkl"

        try:
            self.read_from_file()
        except ValueError:
            print("Kunde inte läsa in filen " + self.filnamn)

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

    def save_to_fil(self):
         self.elevlist = sorted( self.elevlist, key=lambda p: p.namn )

         with open (self.filnamn, "wb") as f:
             pickle.dump(self.elevlist, f)

    def spara_avsluta(self):
        self.save_to_fil()

    def read_from_file(self):

        #om filen saknas 
        if not os.path.exists(self.filnamn):
            with open(self.filnamn, "w") as f:
                f.write("")
    
        else:
            #öppnar fil för läsning
            with open(self.filnamn, "rb") as f:
                elever = pickle.load(f)
                self.elevlista=elever