
"""wargame.gameunit

Ovaj modul sadrži implementaciju GameUnit klase.
"""

import random 

from gameutils import print_bold, weighted_random_selection
from gameuniterror import GameUnitError


class GameUnit:
    """Bazna klasa za stvaranje likova u igri
    
    Stavite opis metode i parametre (argumenti ili atributi) i što funkcija vraća. 
    
    """
    def __init__(self, name=''):
        self.max_hp = 0 # max. udarni bodovi
        self.health_meter = 0 # zdravometar :-) 
        self.name = name      # ime jedinice
        self.neprijatelj = None  # je li jedinica neprijatelj?
        self.unit_type = None    # tip jedinice

    def info(self):
        """Ispisi informaciju o igracu/neprijatelju
        Još nije implementirana.
        """

        pass

    def attack(self, neprijatelj):
        """Glavna logika za 'napad' neprijateljske jedinice

        Stavite opis metode, parametre, seealso i todo.

        
        """
        injured_unit = weighted_random_selection(self, neprijatelj) # odaberi GameUnit objekt ili neprijatelja
        injury = random.randint(10, 15) # kolicina ozlijede
        # azuriraj kolicinu ozlijede
        injured_unit.health_meter = max(injured_unit.health_meter - injury, 0)        
        print("NAPAD! ", end='')
        # ispisi stanje zdravlja sebe i neprijatelja
        self.show_health(end='  ')
        neprijatelj.show_health(end='  ')

    def heal(self, heal_by=2, full_healing=True):
        """Metoda za ozravljanje lika.

        Stavite opis metode, parametre, seealso i todo.
        """
        if self.health_meter == self.max_hp:
            return

        if full_healing:
            self.health_meter = self.max_hp
        else:
            self.health_meter += heal_by
            # nasa iznimka
            if self.health_meter > self.max_hp:
                #raise HealthMeterException()
                pass

        print_bold("Izliječen si!", end=' ')
        self.show_health(bold=True)

    def reset_health_meter(self):
        """Resetiranje mjeraca zdravlja"""
        self.health_meter = self.max_hp

    def show_health(self, bold=False, end='\n'):
        """Ispisi informaciju o zdravlju.

        Stavite opis metoda, parametre, seealso i todo.
        """
        msg = "Zdravlje: {}: {}".format(self.name, self.health_meter)

        if bold:
            print_bold(msg, end=end)
        else:
            print(msg, end=end)