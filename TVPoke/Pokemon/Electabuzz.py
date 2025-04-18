from TVPoke.BaseClasses.PokeTypes import Electric
from TVPoke.BaseClasses.Move import Move

class Electabuzz(Electric):
    def __init__(self):
        moves = [
            Move("Quick Attack", "NORMAL", 40),
            Move("Giga Impact", "NORMAL", 150),
            Move("Discharge", "ELECTRIC", 80),
            Move("Thunder Punch", "ELECTRIC", 75)
        ]
        super().__init__("Electabuzz", 65, moves, "./TVPoke/Pokemon/imgs/Electabuzz.png")