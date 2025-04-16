from TVPoke.BaseClasses.PokeTypes import Psychic
from TVPoke.BaseClasses.Move import Move

class Mew(Psychic):
    def __init__(self):
        moves = [
            Move("Psyshock", "PSYCHIC", 60),
            Move("Psychokinesis", "DARK", 40),
            Move("Dark Pulse", "DARK", 80),
            Move("Amnesia", "PSYCHIC", 0)
        ]
        super().__init__("Mew", 100, moves, "./TVPoke/Pokemon/imgs/Mew.png")