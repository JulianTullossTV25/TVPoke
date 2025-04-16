from TVPoke.BaseClasses.PokeTypes import Water
from TVPoke.BaseClasses.Move import Move

class Blastoise(Water):
    def __init__(self):
        moves = [
            Move("Body Slam", "NORMAL", 40),
            Move("Water Cannon", "WATER", 30),
            Move("Power Wash", "WATER", 50),
            Move("Quake", "ROCK", 20)
        ]
        super().__init__("Blastoise", 80, moves, "./TVPoke/Pokemon/imgs/Blastoise.png")