from TVPoke.BaseClasses.PokeTypes import Electric
from TVPoke.BaseClasses.Move import Move

class Zapdos(Electric):
    def __init__(self):
        moves = [
            Move("Thunderbolt", "ELECTRIC", 90),
            Move("Air Cutter", "FLYING", 60),
            Move("Heat Wave", "FIRE", 100),
            Move("Ominous Wind", "GHOST", 60) # does there need to be types that are needed to be created 
        ]
        super().__init__("Zapdos", 140, moves, "./TVPoke/Pokemon/imgs/Zapados.png")
        
        