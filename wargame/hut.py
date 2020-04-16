from gameutils import print_bold


class Hut:
    """Klasa za kreiranje kucica"""
    def __init__(self, number, occupant):
        self.occupant = occupant
        self.number = number
        self.is_acquired = False

    def acquire(self, new_occupant):
        """Azuriranje okupanta u kucici"""
        self.occupant = new_occupant
        self.is_acquired = True
        print_bold("Kucica broj {} zauzeta".format(self.number))

    def get_occupant_type(self):
        """Vraca tekst s opisom je li je kucica zauzeta ili slobodna"""
        if self.is_acquired:
            occupant_type = 'ZAUZETA'
        elif self.occupant is None:
            occupant_type = 'slobodna'
        else:
            occupant_type = self.occupant.unit_type

        return occupant_type