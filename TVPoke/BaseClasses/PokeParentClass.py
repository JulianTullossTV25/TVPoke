class Pokemon:
    def __init__(self, name, hp, type, critType, moves, imgPath):
        self.name = name
        self.hp = hp
        self.type = type
        self.critType = critType
        self.moves = moves
        self.img = imgPath

        self.stats = {
        "healthPoints" : None,
        "attack" : None,
        "defense" : None,
        "specialAttack" : None,
        "specialDefense" : None,
        "speed" : None
        }

    def takeDamage(self, move, attacker):
        multi = 1
        if move.type == self.critType:
            multi = 2
    

        self.hp -= multi * move.power