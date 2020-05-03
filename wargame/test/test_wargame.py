import unittest
from unittest import mock

from knight import Knight
from orcrider import OrcRider
from gameunit import GameUnit
from gameutils import weighted_random_selection
from hut import Hut
from attackoftheorcs import AttackOfTheOrcs


class TestWarGame(unittest.TestCase):
    """klasa sadrži jedinične testove za aplikaciju AttackOfTheOrcs"""

    def setUp(self):
        """priprema za testove"""
        self.knight = Knight()
        self.enemy  = OrcRider()

    def test_injured_unit_selection(self):
        """jedinicni test za ozlijedjenog lika
        test: vraća li `weighted_random_selection` uvijek GameUnit instancu?
        """
        for i in range(100):
            injured_unit = weighted_random_selection(self.knight,self.enemy)

            self.assertIsInstance(
                injured_unit,
                GameUnit,
                "ozlijedjena jedinica mora biti instanca od `GameUnit`"
            )
    

    def test_acquired_hut(self):
        """Jedinični test za provjeru okupanta kućice nakon što je osvojena.

        Jedinični test koji osigurava da u slučaju kada je kućica `acquired`, instanca `htu.occupant`
        jest instanca od `Knight`
        """

        print('\nPozivamo test za kućicu ...')
        hut = Hut(4,None)
        hut.acquire(self.knight)
        self.assertIs(hut.occupant,self.knight) 


    def test_play(self):
        """Jedinicni test za provjeru unosa u `play` metodi"""
        game = AttackOfTheOrcs()
        self.hut_selection_counter = 0
        with mock.patch('builtins.input',new=self.user_input_processor ) as foo_patch:
            foo_patch = self.user_input_processor
            game.play()
            # prikupi listu okupiranih kućica
            acquired_hut_list = [h.is_acquired for h in game.huts]

            # igrac pobjedjuje ako je osvojio sve kućice
            if all(acquired_hut_list):
                # kriterij za pobjedu
                self.assertTrue(game.player.health_meter > 0)
            else:
                # kriterij za gubljenje: igračevo zdravlje ne može biti >0
                self.assertFalse(game.player.health_meter > 0)



    def user_input_processor(self,prompt):
        """simulira korisnicki unesene unose 
        :param prompt: Pitanje postavljeno korisniku
        :return: simulirani korisnički unos
        """
        # sto se nalazi u upitu aplikacije        
        if 'kucice' in prompt.lower():
            # ako se u upitu nalazi 'hut' onda znaci da moramo unijeti broj kućice
            self.hut_selection_counter += 1
            assert self.hut_selection_counter <= 5
            return self.hut_selection_counter
        elif 'napadom' in prompt.lower():
            # pita se hocemo li nastaviti igru
            return 'd'
        else:
            raise Exception('Imam neočekivani upit (prompt):',prompt)

    def test_occupy_huts(self):
        """Jedinicni test za provjeru broja kućica i okupanata"""
        game = AttackOfTheOrcs()
        game.setup_game_scenario()

        # provjeri da je samo 5 kućica 
        self.assertEqual(len(game.huts),5)

        # okupanti kućice moraju biti instance klase GameUnit ili OrcRider
        for hut in game.huts:
            assert((hut.occupant is None) or isinstance(hut.occupant,GameUnit))

if __name__ == '__main__':
    unittest.main()