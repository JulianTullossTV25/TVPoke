from TVPoke.BaseClasses.PokeTypes import Electric
from TVPoke.BaseClasses.Move import Move

class Jolteon(Electric):
    def __init__(self):
        moves = [
            Move("Double Kick", "ELECTRIC", 40),
            Move("ElectricGun", "ELECTRIC", 60),
            Move("Flash Ray", "ELECTRIC", 70),
            Move("Max Thunder Rumble", "ELECTRIC", 100)
        ]
        super().__init__("Jolteon", 160, moves, "./TVPoke/Pokemon/imgs/Jolteon.png")