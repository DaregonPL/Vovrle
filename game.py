from Choice import Choice
import random
import json
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
                raise Exception('Когда тебя спрашивают о твоём' +
                                ' имени, молчать невежливо.')
            self.data['user'] = name
            self.data['scores'][name] = self.data['scores'].get(name, 0)
            self.save()

        self.user = self.data['user']
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
            'Играть', 'На стройку', 'Сохраниться и уйти в закат'
        ], f'{self.user}, вэлком ту Vovrle', ['help', 'helper'],
            upstring=f"{self.user} счет: {self.data['scores'][self.user]}")
        cmm.display()
        ans = cmm.answer()
        if ans == 'Играть':
            self.setup()
        elif ans == 'На стройку':
            cs = Choice(['Назначить другое имя (счётчик сотрется)',
                         'Сменить язык', 'Восстановить игру'],
                        "Настройки", ['home'])
            cs.display()
            ans = cs.answer()
            if ans == 'Назначить другое имя (счётчик сотрется)':
                print('Если чё, счётчик вернётся если поставите старое имя.' +
                      ' Мы, аристократы, пихаем систему аккаунтов везде')
                self.data['user'] = None
                self.save()
                self.__init__()
            elif ans == 'Сменить язык':
                lc = Choice(list(self.lang.keys()), 'Выберите язык')
                lc.display()
                ans = lc.answer()
                if ans != 'home':
                    self.data['gamelang'] = ans
                    self.save()
                    self.__init__()
            elif ans == 'Восстановить игру':
                print('Эх, были бы бэкапы...')
        elif ans == 'Сохраниться и уйти в закат':
            self.save()
            self.exit = True
            print('бай бай')
        elif ans == 'help':
            print('''Vovrle - Wordle, но хуже (v1.0)
разработано VovLer'ом

КАК ВЫБИРАТЬ ПУНКТЫ
Напишите номер пункта или его название и жмакните enter

КАК ИГРАТЬ
Просто погуглите как играть в Wordle. Мне лень писать полмегабайта текста
''')
        elif ans == 'helper':
            print('Запустите helper.py')
        else:
            print('Error01: answer is not defined')

    def setup(self):
        while True:
            cdiff = Choice(list(self.diff.keys()) + ['Пользовательская'],
                           'Выберите сложность:', ['home'])
            cdiff.display()
            ans = cdiff.answer()
            if ans == 'home':
                break
            elif ans == 'Пользовательская':
                leng = input('Ведите длину:')
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
        print(f'Длинна слова - {self.wordln}')
        print('''  Commands:
/q - сдаться
  Highlights:
"-" - буква поставлена не там
"=" - буква поставлена там

Напишите слово маленькими буквами.
Попробуйте угадать исходное слово за 6 попыток:
''')
        a = ''
        for x in range(1, 7):
            a = input('>')
            if a == '/q':
                self.loose('Вы смылись!', word)
                break
            if len(a) != self.wordln:
                self.loose('Неверная длина!', word)
                break
            print(' ' + self.analyze(word, a))
            if word == a:
                self.win()
                break
        if a != word:
            self.loose('Попытки закончились!', word)

    def save(self):
        with open('config.json', 'w', encoding='utf8') as f:
            json.dump(self.data, f, ensure_ascii=False, indent=2)

    def loose(self, reason, word):
        print('- ПРОИГРЫШ -')
        print(reason)
        print(f'Верное слово: {word}')
        print(f'- {round(self.wordln ** 2 / 2)}')
        self.data['scores'][self.user] -= round(self.wordln ** 2 / 2)

    def win(self):
        print('- УРА ПОБЕДА -')
        print(f'+ {self.wordln ** 2 - 2}')
        self.data['scores'][self.user] += self.wordln ** 2 - 2

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
