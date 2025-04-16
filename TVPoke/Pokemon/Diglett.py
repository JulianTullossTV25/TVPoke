from TVPoke.BaseClasses.PokeTypes import Ground
from TVPoke.BaseClasses.Move import Move

class Diglett(Ground):
    def __init__(self):
        moves = [
            Move("Mud-Slap", "GROUND", 10),
            Move("Dig", "GROUND", 10),
            Move("Scratch", "GROUND", 10),
            Move("Headbut Bounce", "GROUND", 10)
        ]
        super().__init__("Diglett", 50, moves, "./TVPoke/Pokemon/imgs/Diglett.png") 