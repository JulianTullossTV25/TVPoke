from TVPoke.BaseClasses.PokeTypes import Normal
from TVPoke.BaseClasses.Move import Move

class Lickitung(Normal):
    def __init__(self):
        moves = [
            Move("Power Whip", "Grass", 120),
            Move("Rollout", "Rock", 90),
            Move("Slam", "Normal", 80),
            Move("Chip Away", "Normal", 70)
        ]
        super().__init__("Lickitung", 140, moves, "./TVPoke/Pokemon/imgs/Lickitung.png")