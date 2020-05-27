import random

from tkinter import Tk, PhotoImage, IntVar, Label, Radiobutton, messagebox

# slanje poruka
from pubsub import pub


# model
class Model:
    """Model komponenta aplikacije. Definira glavnu logiku programa."""
    def __init__(self):
        self.huts = []
        self.result = ""
        # ispuni kućice
        self.occupy_huts()
    
    def occupy_huts(self):
        """funkcija nasumično raspoređuje okupante kućice."""
        occupants = ['neprijatelj', 'prijatelj', 'slobodno']
        while len(self.huts) < 5:
            self.huts  = [random.choice(occupants) for _ in range(5)]
        print("Okupanti kućice su:", self.huts)

    def enter_hut(self, hut_number):
        """Uđi u kućicu i odredi okupanta.        
        """
        # praćenje
        print("Ulazim u kućicu #:", hut_number)
        hut_occupant = self.huts[hut_number-1]
        # praćenje
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

        # komunikacija: model->controller
        pub.sendMessage("najava pobjednika",data=self.result)



class View:
    """Komponenta pogleda prema MVC arhitekturi. Postavlja GUI i definira događaje.
    """
    def __init__(self,parent):
        # definiraj slike za džunglu i kućicu
        self.village_image = PhotoImage(file="images/Jungle_small.gif")
        self.hut_image = PhotoImage(file="images/Hut_small.gif")

        # referenca na Tk prozor
        self.container = parent
        
        # velicina kucice
        self.hut_width = 40
        self.hut_height = 56

        # definiramo referencu na funkciju koja reagira na odabir radio-buttona
        self.radio_button_pressed = None        

    def setup(self):
        """Postavljanje grafičkog sučelja."""
        # grafički elementi
        self.create_widgets()
        # njihova lokacija
        self.setup_layout()

    def set_callbacks(self,callback_function):
        """postavi dani argument da bude metoda objekta. Alternativni način izmjena poruka."""
        self.radio_btn_pressed = callback_function

    
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



class Controller:
    """Upravljač klasa za igru prema MVC argitekturi."""
    def __init__(self,parent):
        self.parent = parent # referenca na TK roditeljsku klasu
        # definiraj model
        self.model = Model()
        # definiraj pogled
        self.view = View(parent)
        # na koje događaje reagirati?
        self.view.set_callbacks(self.radio_btn_pressed)
        # postavi pogled
        self.view.setup()
        # primaj poruke na temu "najava pobjednika"
        pub.subscribe(self.model_change_handler,"najava pobjednika")


     # komunikacija: view->model 
    def radio_btn_pressed(self):
        """callback funkcija za pritisak radiobutton na pogledu"""
        self.model.enter_hut(self.view.var.get())

    # komunikacija: controller->view nakon izmjene na modelu
    def model_change_handler(self,data):
        self.view.announce_winner(data)
        





if __name__ == '__main__':
   # stvori glavni prozor Tk GUI-a
    mainwin = Tk()
    # definiraj veličinu prozora
    WIDTH = 494
    HEIGHT = 307
    mainwin.geometry("{}x{}".format(WIDTH, HEIGHT))
    mainwin.resizable(0, 0) # postavljamo da se prozor ne može skalirati
    mainwin.title("Napad Orkova v2.1")
    # kontroler upravlja aplikacijom
    game_app = Controller(mainwin)
    mainwin.mainloop() # petlja događaja
