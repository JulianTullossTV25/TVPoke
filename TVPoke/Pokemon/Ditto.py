from TVPoke.BaseClasses.PokeTypes import Normal
from TVPoke.BaseClasses.Move import Move

class Ditto(Normal):
    def __init__(self):
        moves = [
            Move("Transform", "NORMAL", 0),
            Move("Hyper Beam", "NORMAL", 150),  
            Move("Body Slam", "NORMAL", 85),   
            Move("Double-Edge", "NORMAL", 120),     
        ]
        super().__init__("ditto", 48, moves, "./TVPoke/Pokemon/imgs/ditto.png")