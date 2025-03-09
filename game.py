from Choice import Choice
import random
import json
import os
'''
Vovrle - Wordle, but worse
'''


class Game:
    def __init__(self):
        with open('config.json', encoding='utf8') as cnf:
            self.data = json.load(cnf)
        if not self.data['user']:
            print('Кто ты, воин?')
            name = input()
            if not name:
                raise Exception('Когда тебя спрашивают о твоём имени, молчать невежливо. Лови эксэпшн бич')
            self.data['user'] = name
            self.save()

        self.lang = self.data['lang']
        self.diff = self.data['diff']
        self.wordln = 0
        self.gamelang = self.data['gamelang']
        self.exit = False
        self.words = None
        while not self.exit:
            self.menu()

    def menu(self):
        cmm = Choice([
            'Play', 'Settings', 'Save', 'Save & Exit'
        ], f'Welcome to Vovrle', ['help', 'about'])
        cmm.display()
        ans = cmm.answer()
        if ans == 'Play':
            self.setup()
        elif ans == 'Settings':
            pass
        elif ans == 'Save':
            self.save()
        elif ans == 'Save & Exit':
            self.save()
            self.exit = True
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
        print(word)
        print(f'Lenght of the word - {self.wordln}')
        print('''  Commands:
/q - give up
/helper - open helper in another window
  Highlights:
"-" - letter positioned wrong
"=" - letter positioned correct

Type the word. You've got 6 attempts:
''')
        for x in range(1, 7):
            a = input('>')
            if a == '/q':
                self.loose('Вы смылись!')
                break
            if len(a) != self.wordln:
                self.loose('Неверная длина!')
                break
            print(' ' + self.analyze(word, a))
            if word == a:
                self.win()
                break

    def save(self):
        with open('config.json', 'w', encoding='utf8') as f:
            json.dump(self.data, f, ensure_ascii=False, indent=2)

    def loose(self, reason):
        print('- ПРОИГРЫШ -')
        print(reason)
        print(f'- {round(self.wordln ** 2 / 2)}')

    def win(self):
        print('- УРА ПОБЕДА -')
        print(f'+ {self.wordln ** 2 - 2}')

    def analyze(self, word, ans):
        res = [' ' for x in range(self.wordln)]
        notfoundlet = list(word)
        for x in range(self.wordln):
            if word[x] == ans[x]:
                res[x] = '='
                notfoundlet.remove(ans[x])
        for x in range(self.wordln):
            if ans[x] in notfoundlet and res[x] != '=':
                res[x] = '-'
                notfoundlet.remove(ans[x])
        return ''.join(res)

    def find_word(self):
        with open(self.lang[self.gamelang], encoding='utf8') as wordfile:
            self.words = wordfile.read().strip().split()
        words = list(filter(lambda a: len(a) == self.wordln, self.words))
        return random.choice(words)


if __name__ == '__main__':
    Game()
