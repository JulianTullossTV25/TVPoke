from TVPoke.BaseClasses.PokeTypes import Water
from TVPoke.BaseClasses.Move import Move

class Vaporeon(Water):
    def __init__(self):
        moves = [
            Move("Blizzard", "ICE", 110),
            Move("Hyper Beam", "NORMAL", 150),
            Move("Double-Edge", "ICE", 120),
            Move("Surf", "WATER", 90)
        ]
        super().__init__("Vaporeon", 80, moves, "./TVPoke/Pokemon/imgs/Vaporeon.png")