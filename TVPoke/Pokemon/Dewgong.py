from TVPoke.BaseClasses.PokeTypes import Water
from TVPoke.BaseClasses.Move import Move

class Dewgong(Water):
    def __init__(self):
        moves = [
            Move("Ice Shard", "ICE", 80),
            Move("Aurora", "WATER", 70),
            Move("Cold Breath", "Ice", 10),
            Move("Tail Whap", "WATER", 60)
        ]
        super().__init__("Dewgong", 100, moves, "./TVPoke/Pokemon/imgs/Dewgong.png")