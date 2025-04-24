import importlib
from PyUI.PageElements import Label, Image

class Trainer:
    def __init__(self, pokemon):
        self.pokemon = []
        for poke in pokemon:
            pokeFile = importlib.import_module("TVPoke.Pokemon." + poke)
            PokeClass = getattr(pokeFile, poke)
            self.pokemon.append(PokeClass())
        self.position = 1
        self.name = ""

    def removeFaintedPokemon(self):
        for poke in self.pokemon:
            if poke.hp <= 0:
                self.pokemon.remove(poke)

    def getElements(self):
        elements = []
        if len(self.pokemon) > 0:
            pokeHealth = self.pokemon[0].hp
            pokeName = self.pokemon[0].name
            pokeImg = self.pokemon[0].img

            if self.position == 1:
            
                pokeX = 25
                pokeY = 15

                pokemon = Image((pokeX, pokeY), 50, 50, pokeImg)
                healthLabel = Label((25, 15), 20, 10, pokeName + " HP: " + str(pokeHealth))
            else:
                pokeX = 75
                pokeY = 45

                pokemon = Image((pokeX, pokeY), 20, 20, pokeImg)
                healthLabel = Label((25, 80), 20, 10, pokeName + " HP: " + str(pokeHealth))

            elements.append(pokemon)
            elements.append(healthLabel)
            return elements
        else:
            return elements