from TVPoke.BaseClasses.PokeTypes import Dragon
from TVPoke.BaseClasses.Move import Move

class Dragonite(Dragon):
    def __init__(self):
        moves = [
            Move("Dragon Rush", "DRAGON", 100),
            Move("Extreme Speed", "NORMAL", 80),
            Move("Agility", "PSYCHIC", 0),
            Move("Fire Punch", "FIRE", 75)
        ]
        super().__init__("Dragonite", 91, moves, "./TVPoke/Pokemon/imgs/Dragonite.png")