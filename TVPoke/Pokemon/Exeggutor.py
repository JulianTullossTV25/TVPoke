from TVPoke.BaseClasses.PokeTypes import *
from TVPoke.BaseClasses.Move import Move

class Exeggutor(Grass):
    def __init__(self):
        moves = [
            Move("Psyshock", "Psychic", 80),
            Move("Stomp", "NORMAL", 65),
            Move("Seed Bomb", "Grass", 80),
            Move("Sludge Bomb", "Poison", 90 )
        ]
        super().__init__("Exeggutor", 85, moves, "./TVPoke/Pokemon/imgs/Exeggutor.png")