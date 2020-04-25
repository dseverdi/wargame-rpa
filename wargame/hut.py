
"""wargame.hut

Ova je implementacija kompatibilna s Python 3.6+ verzijom.

:copyright: None
:licence: None
"""


from gameutils import print_bold


class Hut:
    # RST stil pisanja dokumentacije
    """Klasa koja prezentira kucicu.

    :arg int number: broj kucice 
    :arg AbstractGameUnit occupant: Tip okupanta kucice

    :ivar int number: broj pridruzen kucici
    :ivar boolean is_acquired: je li kucica osvojena od igraca Taliona
    :ivar AbstractGameUnit occupant: Okupant kucice.
                   Mora biti instanca klase
                  `AbstractGameUnit`.

    .. seealso:: gdje se još koristi --
            :py:meth:`attackoftheorcs.AttackOfTheOrcs.setup_game_scenario`
    """

    def __init__(self, number, occupant):
        self.occupant = occupant
        self.number = number
        self.is_acquired = False

    def acquire(self, new_occupant):
        """Ažuriraj okupanta kućice i promijeni status `is_acquired`.

        Ažuriraj varijablu instance za okupanta s parametrom `new_occupant`
                
        :arg new_occupant: self.occupant će se ažurirati s ovim parametrom

        .. todo:: U trenutačnoj implementaciji samo vitez može zatražiti kućicu.
                  Plan je dodati mogućnost i za neprijatelja.
        """
        self.occupant = new_occupant
        
        self.is_acquired = True
        print_bold("Kucica broj {} zauzeta".format(self.number))

    def get_occupant_type(self):
        """Vraca tekst s opisom o vrsti zauzeća kućice.
        
        Koristi se za ispis informacije tko je prisutan u kućici. 
        Informaciju koju vrati ovisi o okupantu i može biti: 
        'neprijatelj', 'prijatelj', 'ZAUZETA','slobodna'.        

        :return: string koji predstavlja vrstu okupanta
        .. sealso: :py:meth:`attackoftheorcs.AttackOfTheOrcs.get_occupants`
        """
        if self.is_acquired:
            occupant_type = 'ZAUZETA'
        elif self.occupant is None:
            occupant_type = 'slobodna'
        else:
            occupant_type = self.occupant.unit_type

        return occupant_type