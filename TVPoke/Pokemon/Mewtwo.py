from TVPoke.BaseClasses.PokeTypes import Psychic
from TVPoke.BaseClasses.Move import Move

class Mewtwo(Psychic):
    def __init__(self):
        moves = [
            Move("Future Sight", "Psychic", 120),
            Move("Psystrike ", "Psychic", 100),
            Move("Psychic", "Psychic", 80),
            Move("Psycho Cut", "Psychic", 70)
        ]
        super().__init__("mewtwo", 106, moves, "./TVPoke/Pokemon/imgs/Mewtwo.png")