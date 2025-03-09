from Choice import Choice
import random
'''
Vovrle - Wordle, but worse
'''


class Game:
    def __init__(self):
        self.lang = {  # Name: path
            'Russian': 'words/russian.dict',
            'English': 'words/english.dict'
        }
        self.diff = {  # Name: len
            'Easy (5 symbols)': 5,
            'Medium (6 symbols)': 6,
            'Hard (7 symbols)': 7,
            'Extra Hard (8 symbols)': 8
        }
        self.wordln = 0
        self.gamelang = 'Russian'
        self.exit = False
        while not self.exit:
            self.menu()

    def menu(self):
        cmm = Choice([
            'Play', 'Settings', 'Save & Exit'
        ], 'Welcome to Vovrle', ['help', 'about'])
        cmm.display()
        ans = cmm.answer()
        if ans == 'Play':
            self.setup()
        elif ans == 'Settings':
            pass
        elif ans == 'Save & Exit':
            pass
        elif ans == 'help':
            pass
        elif ans == 'about':
            pass
        else:
            print('Error01: answer is not defined')

    def setup(self):
        while True:
            cdiff = Choice(list(self.diff.keys()) + ['Custom'], 'Choose Difficulty', ['home'])
            cdiff.display()
            ans = cdiff.answer()
            if ans == 'home':
                break
            elif ans == 'Custom':
                leng = input('Enter lenght:')
                if leng.isdigit():
                    self.wordln = int(leng)
                    self.play()
                    break
                else:
                    print('Invalid Input: int expected')
            else:
                self.wordln = self.diff[ans]
                self.play()
                break

    def play(self):
        word = self.find_word()
        print(f'Word: {word}')

    def find_word(self):
        with open(self.lang[self.gamelang], encoding='utf8') as wordfile:
            words = wordfile.read().strip().split()
        words = list(filter(lambda a: len(a) == self.wordln, words))
        return random.choice(words)


if __name__ == '__main__':
    Game()
