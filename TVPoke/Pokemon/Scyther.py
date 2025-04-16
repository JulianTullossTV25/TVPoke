from TVPoke.BaseClasses.PokeTypes import Bug
from TVPoke.BaseClasses.Move import Move

class Scyther(Bug):
    def __init__(self):
        moves = [
            Move("X Scissor", "BUG", 80),
            Move("Fury Cutter", "BUG", 40),
            Move("Slash", "NORMAL", 70),
            Move("Quick Attack", "NORMAL", 40)
        ]
        super().__init__("Scyther", 80, moves, "./TVPoke/Pokemon/imgs/Scyther.png")