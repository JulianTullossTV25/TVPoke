from TVPoke.BaseClasses.PokeTypes import Normal
from TVPoke.BaseClasses.Move import Move

class Snorlax(Normal):
    def __init__(self):
        moves = [
            Move("Body Slam", "NORMAL", 120),
            Move("Outrage", "NORMAL", 120),
            Move("Frustration", "NORMAL", 0),
            Move("Skull Bash", "NORMAL", 130)
        ]
        super().__init__("Snorlax", 160, moves, "./TVPoke/Pokemon/imgs/Snorlax.png")