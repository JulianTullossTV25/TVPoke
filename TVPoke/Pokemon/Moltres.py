from TVPoke.BaseClasses.PokeTypes import Fire
from TVPoke.BaseClasses.Move import Move

class Moltres(Fire):
    def __init__(self):
        moves = [
            Move("Searing Flame", "FIRE", 20),
            Move("Fire Spin", "FIRE", 180),
            Move("Blazing Flight", "FIRE", 0),
            Move("Fire Wing", "FIRE", 110)
        ]
        super().__init__("Moltres", 100, moves, "./TVPoke/Pokemon/imgs/Moltres.png")