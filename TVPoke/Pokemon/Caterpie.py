from TVPoke.BaseClasses.PokeTypes import Bug
from TVPoke.BaseClasses.Move import Move

class Caterpie(Bug):
    def __init__(self):
        moves = [
            Move("Tackle", "NORMAL", 40),
            Move("Bug bite", "BUG", 60),
            Move("String Shot", "BUG", 0)
        ]
        super().__init__("Caterpie", 45, moves, "./TVPoke/Pokemon/imgs/Caterpie.png")