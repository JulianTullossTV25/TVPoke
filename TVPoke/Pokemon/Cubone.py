from TVPoke.BaseClasses.PokeTypes import Ground
from TVPoke.BaseClasses.Move import Move

class Cubone(Ground):
    def __init__(self):
        moves = [
            Move("Mud Slap", "GROUND", 100),
            Move("Thrash", "NORMAL", 100),
            Move("Headbutt", "NORMAL", 100),
            Move("Bone rush", "GROUND", 90)
        ]
        super().__init__("Cubone", 304, moves, "./TVPoke/Pokemon/imgs/Cubone.png")