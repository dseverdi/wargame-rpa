"""wargame.knight

Ovaj modul sadrži klasu koja implementira viteza.

:copyright: 2020, None

:license: The MIT License (MIT) . 
"""


from gameutils import print_bold
from gameunit import GameUnit

class Knight(GameUnit):
    """ Klasa koja predstavlja Viteza, lika u igri.
    Stavite opis metode, parametre i atribute, seealso i todo.
    
    """
    def __init__(self, name='Vitez Talion'):
        super().__init__(name=name) # poziv konstruktora bazne klase
        # ili ...
        # GameUnit.__init__(self,name)
        self.max_hp = 40 # definiraj max hit points
        self.health_meter = self.max_hp  # postavi zdravometar :-) 
        self.unit_type = 'prijatelj'  # status jedinice

    def info(self):
        """Ispiši osnovne informacije o liku.
        """

        print("Ja sam vitez!")

    def acquire_hut(self, hut):
        """Borba za kucicu.

        Stavite opis metode, parametre i atribute, seealso i todo.
       """
        print_bold("Ulazim u kucicu broj %d..." % hut.number, end=' ')
        is_neprijatelj = (isinstance(hut.occupant, GameUnit) and
                    hut.occupant.unit_type == 'neprijatelj')
        continue_attack = 'd'
        if is_neprijatelj:
            print_bold("Neprijatelj na vidiku!")
            self.show_health(bold=True, end=' ')
            hut.occupant.show_health(bold=True, end=' ')
            while continue_attack:
                continue_attack = input(".......nastavi s napadom? (d/n): ")
                if continue_attack == 'n':
                    self.run_away()
                    break
                # napadaj dok je 'd' upisan
                elif continue_attack == 'd':
                    self.attack(hut.occupant)
                    # ukoliko zdravlje neprijatelja padne na 0 ili manje
                    if hut.occupant.health_meter <= 0:
                        print("")
                        # zauzmi kucicu
                        hut.acquire(self)
                        break
                    if self.health_meter <= 0:
                        print("")
                        break
                
        else:
            if hut.get_occupant_type() == 'slobodna':
                print_bold("Kućica je slobodna")
            else:
                print_bold("Prijatelj na vidiku!")
            hut.acquire(self)
            self.heal()

    def run_away(self):
        """Metoda za napustanje borbe.

        Stavite opis metode, parametre i atribute, seealso i todo.
        """
        print_bold("BJEZANJE...")
        self.neprijatelj = None
