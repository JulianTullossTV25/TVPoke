from TVPoke.BaseClasses.PokeTypes import Water
from TVPoke.BaseClasses.Move import Move

class Psyduck(Water):
    def __init__(self):
        moves = [
            Move("Aqua Tail", "WATER", 90),
            Move("Zen Headbutt", "PSYCHIC", 80),
            Move("Water Pulse", "WATER", 60),
            Move("Confusion", "PSYCHIC", 50)
        ]
        super().__init__("Psyduck", 80, moves, "./TVPoke/Pokemon/imgs/Psyduck.png")