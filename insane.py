import random
class Insane:
    def __init__(self):
        self.value1 = 0
        self.value2 = 0
        self.sum = 0
        self.IsThere7 = False
    def Roll(self):
        self.value1 = random.randint(1,6)
        self.value2 = random.randint(1,6)
        print("Value of the first die is:")
        print(self.value1)
        print("Value of the second die is:")
        print(self.value2)
        return self.value1, self.value2
    def Sum(self):
        self.sum = self.value1 + self.value2
        print("The sum of the dice is:")
        print(self.sum)
        return self.sum
    def Check7(self):
        if self.sum == 7:
            self.IsThere7 = True
        print("Is there a 7 drawn?")
        print(self.IsThere7)
        if self.IsThere7 == True:
            print("You lose.")
        else:
            print("You win!")
        return self.IsThere7

class InsaneDriver(Insane):
    def __init__(self):
        Insane.__init__(self)
        self.game = Insane()
    def PlayAGame(self):
        self.game.Roll()
        self.game.Sum()
        self.game.Check7()

x = InsaneDriver()
x.PlayAGame()