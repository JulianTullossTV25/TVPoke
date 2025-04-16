from TVPoke.BaseClasses.PokeTypes import Fire
from TVPoke.BaseClasses.Move import Move

class Flareon(Fire):
    def __init__(self):
        moves = [
            Move("Fire Fang", "FIRE", 50),
            Move("Flame Thrower", "FIRE", 60),
            Move("Flare Blitz", "FIRE", 60),
            Move("Body Slam", "NORMAL", 45)
        ]
        super().__init__("Flareon", 75, moves, "./TVPoke/Pokemon/imgs/Flareon.png")