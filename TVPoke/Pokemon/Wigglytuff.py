from TVPoke.BaseClasses.PokeTypes import Fairy
from TVPoke.BaseClasses.Move import Move

class Wigglytuff(Fairy):
    def __init__(self):
        moves = [
            Move("Pound", "NORMAL", 40),
            Move("Double Edge", "NORMAL", 120),
            Move("Play Rough", "FAIRY", 90),
            Move("Round", "NORMAL", 60)
            
        ]
        super().__init__("Wigglytuff", 140, moves, "./TVPoke/Pokemon/imgs/Wigglytuff.png")