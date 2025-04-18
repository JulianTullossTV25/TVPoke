from TVPoke.BaseClasses.PokeTypes import Fire
from TVPoke.BaseClasses.Move import Move

class Charmander(Fire):
    def __init__(self):
        moves = [
            Move("Scratch", "NORMAL", 10),
            Move("Ember", "FIRE", 40),
            Move("Take down", "NORMAL", 90),
        ]
        super().__init__("Charmander", 120, moves, "./TVPoke/Pokemon/imgs/Charmander.png")