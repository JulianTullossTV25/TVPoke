from TVPoke.BaseClasses.PokeTypes import *
from TVPoke.BaseClasses.Move import Move

class Magikarp(Water):
    def __init__(self):
        moves = [
            Move("Splash", "NORMAL", 0),
            Move("Tackle", "NORMAL", 40),
            Move("Hydro Pump", "WATER", 110),
            Move("Bounce", "FLYING", 85)
        ]
        super().__init__("Magikarp", 20, moves, "./TVPoke/Pokemon/imgs/Magikarp.png")