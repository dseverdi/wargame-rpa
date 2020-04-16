
from gameunit import GameUnit

class OrcRider(GameUnit):
    """Klasa koja predstavlja lika Orc Rider"""
    def __init__(self, name=''):
        super().__init__(name=name)
        self.max_hp = 30
        self.health_meter = self.max_hp
        self.unit_type = 'neprijatelj'
        self.hut_number = 0

    def info(self):
        print("Grrrr..Ja sam Orc Wolf Rider.")