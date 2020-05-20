from tkinter import Tk, Label, Radiobutton, PhotoImage, IntVar
from tkinter import messagebox

import random

class HutGame:
    def __init__(self, parent):
        """Igra u kojoj igrač odabire kućicu u kojoj će se Talion odmoriti.

        Program inicijalno stavlja 'neprijatelja' ili 'prijatelja' u svaku od kućica. 
        Neke kućice mogu biti nenastanjene. 
        Od igrača se očekuje da odaber kućicu u kojoj će smjestiti Taliona. Pobjeđuje se 
        ako je okupant kućice 'prijatelj' ili kućica nije nastanjena                
        """

        # definiraj slike za džunglu i kućicu
        self.village_image = PhotoImage(file="images/Jungle_small.gif")
        self.hut_image = PhotoImage(file="images/Hut_small.gif")
        
        self.hut_width = 40
        self.hut_height = 56
        self.container = parent

        self.huts = []
        self.result = ""
        # punjenje kućica
        self.occupy_huts()
        # postavi korisničko sučelje
        self.setup()

# ------------- ne-GUI metode -----------------------------------
    def occupy_huts(self):
        """funkcija nasumično raspoređuje okupante kućice ."""
        occupants = ['neprijatelj', 'prijatelj', 'slobodno']
        while len(self.huts) < 5:
            self.huts  = [random.choice(occupants) for _ in range(5)]
        print("Okupanti kućice su:", self.huts)

    def enter_hut(self, hut_number):
        """Uđi u kućicu i odredi okupanta.        
        """

        print("Ulazim u kućicu #:", hut_number)
        hut_occupant = self.huts[hut_number-1]
        print("Okupant kućice je: ", hut_occupant)

        if hut_occupant == 'neprijatelj':
            self.result = "neprijatelj je u kućici # {} \n\n".format(hut_number)
            self.result += "IZGUBIO SI :( Više sreće drugi put!"
        elif hut_occupant == 'slobodno':
            self.result = "Kućica # {} je slobodna\n\n".format(hut_number)
            self.result += "Čestitke! POBIJEDILI STE!!!"
        else:
            self.result = "prijatelj je u kućici # {} \n\n".format(hut_number)
            self.result += "Čestitke! POBIJEDILI STE!!!"

        # Proglasi pobjednika!
        self.announce_winner(self.result)

#----------------- GUI metode --------------------------------------
    def create_widgets(self):
        """stvori grafičke elemente unutar glavnog prozora"""
        self.var = IntVar()
        self.background_label = Label(self.container,
                                      image=self.village_image)
        txt = "Odaberi kućicu kako bi pobijedio:\n"
        txt += "Kućica je slobodna ili sadrži prijatelja odnosno neprijatelja."
        self.info_label = Label(self.container, text=txt, bg='yellow')
        # rječnik za konfiguraciju radiobutton-a
        r_btn_config = {'variable': self.var,
                        'bg': '#A8884C',
                        'activebackground': 'yellow',
                        'image': self.hut_image,
                        'height': self.hut_height,
                        'width': self.hut_width,
                        'command': self.radio_btn_pressed}

        self.r1 = Radiobutton(self.container, r_btn_config, value=1)
        self.r2 = Radiobutton(self.container, r_btn_config, value=2)
        self.r3 = Radiobutton(self.container, r_btn_config, value=3)
        self.r4 = Radiobutton(self.container, r_btn_config, value=4)
        self.r5 = Radiobutton(self.container, r_btn_config, value=5)

    def setup(self):
        """Postavi sučelje."""
        self.create_widgets()
        self.setup_layout()

    def setup_layout(self):
        """Koristi mrežnu geometriju za postavljanje grafičkih elemenata"""
        # dopuštanje skaliranja veličine specifičnih redaka odnosno stupaca
        self.container.grid_rowconfigure(1, weight=1)
        self.container.grid_columnconfigure(0, weight=1)
        self.container.grid_columnconfigure(4, weight=1)
        # postavljanje glavne oznake (ima ulogu stvaranje pozadine)
        self.background_label.place(x=0, y=0, relwidth=1, relheight=1)
        self.info_label.grid(row=0, column=0, columnspan=5, sticky='nsew') # 5 stupaca zauzeće za info_label
        # postavljanje radiobuttona s obzirom na mrežu
        self.r1.grid(row=1, column=0) 
        self.r2.grid(row=1, column=4)
        self.r3.grid(row=2, column=3)
        self.r4.grid(row=3, column=0)
        self.r5.grid(row=4, column=4)

    def announce_winner(self, data):
        """Proglasi pobjednika
        """
        # messagebox widget
        messagebox.showinfo("Proglašenje pobjednika: ", message=data)

    # Upravljanje s događajima
    def radio_btn_pressed(self):
        """callback funkcija kada se pritisne radiobutton
        """
        self.enter_hut(self.var.get())


if __name__ == "__main__":
    # stvori glavni prozor Tk GUI-a
    mainwin = Tk()
    # definiraj veličinu prozora
    WIDTH = 494
    HEIGHT = 307
    mainwin.geometry("{}x{}".format(WIDTH, HEIGHT))
    mainwin.resizable(0, 0) # postavljamo da se prozor ne može skalirati
    mainwin.title("Napad Orkova v2.0")
    game_app = HutGame(mainwin)
    mainwin.mainloop() # petlja događaja