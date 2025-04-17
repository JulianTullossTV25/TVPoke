from TVPoke.BaseClasses.PokeTypes import Normal
from TVPoke.BaseClasses.Move import Move

class Kangaskhan(Normal):
    def __init__(self):
        moves = [
            Move("Fake Out", "NORMAL", 40, "Physical"),
            Move("Body Slam", "NORMAL", 85, "Physical"),
            Move("Crunch", "DARK", 80, "Physical"),
            Move("Power up Punch", "FIGHTING", 40, "Physical")
        ]
        self.stats = {
        "healthPoints" : 105,
        "attack" : 95,
        "defense" : 80,
        "specialAttack" : 40,
        "specialDefense" : 80,
        "speed" :90
        }
        self.statBuffs = {
        "healthPoints" : 1,
        "attack" : 1,
        "defense" : 1,
        "specialAttack" : 1,
        "specialDefense" : 1,
        "speed" : 1
        }

        super().__init__("Kangaskhan", self.stats["healthPoints"], moves, "./TVPoke/Pokemon/imgs/Kangaskhan.png")
    
