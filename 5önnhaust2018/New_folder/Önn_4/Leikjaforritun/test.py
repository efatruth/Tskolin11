from utilaties import *
import random


# name	: Dice.
# system: FOR3G3U - demo for game programming.
# role	: Embeds the functionality of a single dice.
# desc	: The class contains one member variable and a single function, throw()
# author: Sigurdur R. Ragnarsson
# date	: 11.09.2016
class Dice:
    def __init__(self):
        self.number = 0

    # the throw function assumes a six-sided dice
    # containing numbers(dots) from 1 to and including 6
    def throw(self):
        self.number = random.randint(1, 6)
        return self.number

class DiceThrower:
    def __init__(self, how_many=5):  # default number of dice is 5
        self.number_of_dice = how_many
        self.dice = Dice()
        self.dice_list = [0 for i in range(self.number_of_dice)]

    # throws all the dice contained within dice_list
    def throw(self):
        for x in range(0, self.number_of_dice):
            self.dice_list[x] = self.dice.throw()
        return self.dice_list

    # rethrows the dice contained in the rethrow_list
    def rethrow(self, rethrow_list=[]):
        if 0 < len(rethrow_list) <= self.number_of_dice:
            if min(rethrow_list) >= 0 and max(rethrow_list) <= self.number_of_dice - 1:
                for item in rethrow_list:
                    self.dice_list[item] = self.dice.throw()
            return self.dice_list
        else:
            return self.throw()

# Leikurinn samanstendur af 5 tenginum
dt = DiceThrower()

sheet = [-1,-1,-1,-1,-1]

game_is_on = main_menu()



while game_is_on:

    for i in range(0,5):

        dice = dice_menu(dt)

        sheet_menu(dice,sheet)


    print('Final Score',sum(sheet))
    game_is_on = main_menu()

print('The End!')