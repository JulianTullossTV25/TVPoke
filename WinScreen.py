from PyUI.Screen import Screen
from PyUI.PageElements import *

class WinScreen(Screen):
    def __init__(self, window):
        super().__init__(window, (0, 255, 0))
        self.winner = ""
        self.state = {
            "goTo": ""
        }

    def elementsToDisplay(self):
        self.elements = [
            Label((50, 50), 40, 20, self.winner + " won!", 32, (255, 255, 255)) 
        ]
