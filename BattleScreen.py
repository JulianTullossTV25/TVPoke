from PyUI.Screen import Screen
from TVPoke.BaseClasses.Trainer import Trainer
from PyUI.PageElements import *

class BattleScreen(Screen):
    def __init__(self, window):
        super().__init__(window, (25, 255, 40))
        self.state = {
            "goTo" : ""
        }
        self.trainers = []
        self.loser = ""
        
    def addTrainers(self, trainer1Poke, trainer2Poke):
        self.trainers = [
            Trainer(trainer1Poke),
            Trainer(trainer2Poke)
        ]
        self.activeTrainer = self.trainers[0]
        self.trainers[0].name = "player 1"
        self.trainers[1].name = "player 2"

        for trainer in self.trainers:
            if trainer == self.activeTrainer:
                trainer.position = 1
            else:
                trainer.position = 2

    def checkLoser(self):
        for trainer in self.trainers:
            if len(trainer.pokemon) == 0:
                self.state["goTo"] = "WIN"
                self.loser = trainer.name
                break

    def elementsToDisplay(self):
        self.elements = [
            Arena(),
            Shape((82, 17), 60, 30, [(0, 0), (100, 0), (100, 100), (0, 100)], (100, 100, 100))
        ]

        self.checkLoser()

        for trainer in self.trainers:
            self.elements.extend(trainer.getElements())

        if self.loser != "":
            pass
        else:
            for i, move in enumerate(self.activeTrainer.pokemon[0].moves):
                x = 75 + (i % 2) * 15  
                y = 10 + (i // 2) * 15 
                self.elements.append(AttackButton((x,y), move))



class Arena(Image):
    def __init__(self):
        super().__init__((50, 50), 100, 100, "./imgs/battleground.jpg")


class AttackButton(Button):
    def __init__(self, centerXY, move):
        super().__init__(centerXY, 12, 10, (255,255,255), (0,0,0))
        self.move = move
        self.text = self.move.name

    def onClick(self, screen):
        print("You clicked " + self.move.name + "!")
        print("You dealt " + str(self.move.power) + " damage!")
        for trainer in screen.trainers:
            if trainer != screen.activeTrainer:
                trainer.pokemon[0].takeDamage(self.move)
                trainer.removeFaintedPokemon()
            else:
                pass
        screen.activeTrainer.removeFaintedPokemon()

        if screen.activeTrainer == screen.trainers[0]:
            screen.activeTrainer = screen.trainers[1]
        else:
            screen.activeTrainer = screen.trainers[0]

        for trainer in screen.trainers:
            if trainer == screen.activeTrainer:
                trainer.position = 1
            else:
                trainer.position = 2
    
                




