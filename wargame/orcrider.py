"""wargame.orcrider

Ovaj modul sadrži implmentaciju OrcRider klase.

:copyright: 2020, None

:license: The MIT License (MIT) . 
"""


from gameunit import GameUnit

class OrcRider(GameUnit):
    """Klasa koja predstavlja lika Orc Rider
    
    Stavite opis metode i parametre (argumenti ili atributi) i što funkcija vraća. 
    """
    def __init__(self, name=''):
        super().__init__(name=name)
        self.max_hp = 30
        self.health_meter = self.max_hp
        self.unit_type = 'neprijatelj'
        self.hut_number = 0

    def info(self):
        """Ispisuje osnovnu informaciju o liku."""
        print("Grrrr..Ja sam Orc Wolf Rider.")