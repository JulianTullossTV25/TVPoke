from TVPoke.BaseClasses.PokeTypes import Fire
from TVPoke.BaseClasses.Move import Move

class Magmar(Fire):
    def __init__(self):
        moves = [
            Move("Karate Chop", "FIGHTING", 60),
            Move("Flame Thrower", "FIRE", 90),
            Move("Thunder Punch", "ELECTRIC", 75),
            Move("Fire Punch", "FIRE", 75)
        ]
        super().__init__("Magmar", 65, moves, "./TVPoke/Pokemon/imgs/Magmar.png")