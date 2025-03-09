from Choice import Choice
import random
'''
Vovrle - Wordle, but worse
'''


class Game:
    def __init__(self):
        self.exit = False
        while not self.exit:
            self.menu()

    def menu(self):
        ChoiceMM = Choice([
            'Play', 'Settings', 'Save & Exit'
        ], 'Welcome to Vovrle', ['help', 'about'])
        ChoiceMM.display()
        ans = ChoiceMM.answer()
        if ans == 'Play':
            pass
        elif ans == 'Settings':
            pass
        elif ans == 'Save & Exit':
            pass
        elif ans == 'help':
            pass
        elif ans == 'about':
            pass
        else:
            print('fuvk')


if __name__ == '__main__':
    Game()