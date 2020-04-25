"""wargame.gameuniterror

Modul koji implementira vlastito definirane iznimke.

"""

class HutError(Exception):
    """Prilagođena klasa iznimke za `Hut`.

    Nasljeđuje ugrađenu `Exception` klasu.

    Stavite opis metode i parametre (argumenti ili atributi) i što funkcija vraća. 
    """
    def __init__(self, code):
        self.error_message = ''
        self.error_dict = {
            000: "Kod 000: Nespecificirana greška u programskom kodu za klasu Hut",
            101: "Kod 101: Uneseni broj je izvan zadanog raspona: Broj > 5",
            102: "Kod 102: Uneseni broj je izvan zadanog raspona: Broj nije pozitivan",
            103: "Kod 103: Uneseni broj je izvan zadanog raspona: Broj je 0",
            104: "Kod 104: Unesena vrijednost nije broj"
        }
        try:
            self.error_message = self.error_dict[code]
        except KeyError:
            self.error_message = self.error_dict[000]
        print("\n Opis greške: {}".format(self.error_message))
        