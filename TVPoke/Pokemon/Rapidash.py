from TVPoke.BaseClasses.PokeTypes import Fire
from TVPoke.BaseClasses.Move import Move

class Rapidash(Fire):
    def __init__(self):
        moves = [
            Move("Searing Flame", "FIRE", 20),
            Move("Overrun", "FIRE", 30),
            Move("Fire Mane", "FIRE", 90),
            Move("Agility", "NORMAL", 0)
        ]
        super().__init__("Rapidash", 80, moves, "./TVPoke/Pokemon/imgs/Rapidash.png")