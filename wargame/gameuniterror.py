"""wargame.gameuniterror

Modul koji implementira vlastito definirane iznimke.

"""

class GameUnitError(Exception):
    """prilagođena klasa iznimke za `GameUnit` i njene podklase

    Nasljeđuje ugrađenu `Exception` klasu.

    Stavite opis metode i parametre (argumenti ili atributi) i što funkcija vraća. 
    """
    def __init__(self,msg='',code=000):
        super().__init__(msg)
        self.znakovi = '~'*50+'\n'
        self.error_message = ''
        self.error_dict = {
            000: 'ERROR-000: nespecificirana pogreška',
            102: 'ERROR-102: Problem u napadu! Zanemarujem...'
        }
        try:
            self.error_message = self.znakovi + self.error_dict[code]
        except KeyError:
            self.error_message = self.znakovi + self.error_dict[000]
        self.error_message += '\n'

class HealthMeterException(GameUnitError):
    """prilagođena klasa za zdravometar. 

    Stavite opis metode i parametre (argumenti ili atributi) i što funkcija vraća. 

    """
    def __init__(self, msg=''):
        self.error_message = self.znakovi + 'ERROR-101: Problem sa zdravometrom' +'\n'
        print("Opis greške: {}".format(self.error_message))