from TVPoke.BaseClasses.PokeTypes import Psychic
from TVPoke.BaseClasses.Move import Move

class Alakazam(Psychic):
    def __init__(self):
        moves = [
            Move("Fire Punch", "FIRE", 75),
            Move("Ice Punch", "ICE", 75),
            Move("Psycho Cut", "PSYCHIC", 70),
            Move("Future Sight", "PSYCHIC", 120)
        ]
        super().__init__("Alakazam", 120, moves, "./TVPoke/Pokemon/imgs/Alakazam.png")