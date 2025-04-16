from TVPoke.BaseClasses.PokeTypes import Poison
from TVPoke.BaseClasses.Move import Move

class Muk(Poison):
    def __init__(self):
        moves = [
            Move("Stench", "Poison", 40),
            Move("Sticky Hold", "Poison", 40),
    
        ]
        super().__init__("Muk", 105, moves, "./TVPoke/Pokemon/imgs/Muk.png")