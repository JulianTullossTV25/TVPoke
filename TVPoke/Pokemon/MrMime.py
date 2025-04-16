from TVPoke.BaseClasses.PokeTypes import Grass
from TVPoke.BaseClasses.Move import Move

class MrMime(Grass):
    def __init__(self):
        moves = [
            Move("Pound", "Normal", 40),
            Move("Confusion", "Psychic", 50),
            Move("Dazzling Gleam", "Fairy", 80),
            Move("Substitute", "Normal", 0)
        ]
        super().__init__("Mr Mime", 40, moves, "./TVPoke/Pokemon/imgs/MrMime.png")