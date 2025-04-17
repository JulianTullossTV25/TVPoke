from TVPoke.BaseClasses.PokeTypes import Normal
from TVPoke.BaseClasses.Move import Move

class Pikachu(Normal):
    def __init__(self):
        moves = [
            Move("Electro Ball", "ELECTIRC", 50),
            Move("Scrappy Spark", "ELECTIRC", 30),
            Move("Thunderbolt", "ELECTIRC", 120),
            Move("Spark", "ELECTIRC", 20)
        ]
        super().__init__("Pikachu", 70, moves, "./TVPoke/Pokemon/imgs/Pikachu.png")