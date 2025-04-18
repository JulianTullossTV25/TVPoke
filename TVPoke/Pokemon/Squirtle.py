from TVPoke.BaseClasses.PokeTypes import Water
from TVPoke.BaseClasses.Move import Move

class Squirtle(Water):
    def __init__(self):
        moves = [
            Move("Tail Whip ", "NORMAL", 25),
            Move("Tackle", "NORMAL", 35),
            Move("Water Gun", "WATER", 40),
            Move("Withdraw", "WATER", 0)
        ]
        super().__init__("Squirtle", 44, moves, "./TVPoke/Pokemon/imgs/Squirtle.png")
        