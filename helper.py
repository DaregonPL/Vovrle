import json
import random


def guess(mask, include=None, exclude=None):
    if exclude is None:
        exclude = []
    if include is None:
        include = []
    ln = len(mask)
    with open('config.json', encoding='utf8') as confile:
        cnf = json.load(confile)
    with open(cnf['lang'][cnf['gamelang']], encoding='utf8') as wf:
        words = list(filter(lambda a: len(a) == len(mask), wf.read().strip().split()))
    goodwords = []
    for w in words:
        unused = list(w)
        unfit = 0
        for x in range(ln):
            if mask[x].isalpha():
                if mask[x] != w[x]:
                    unfit = 1
                    break
                unused.remove(w[x])
        if unfit:
            continue
        if len([x for x in unused if x in include]) < len(include):
            continue
        if [x for x in unused if x in exclude]:
            continue
        goodwords.append(w)
    return goodwords


if __name__ == '__main__':
    print('''Это - прога-хэлпер
Ищет подходящие слова по шаблону.
Выбранный язык - язык в игре (сохранен в config.json)

ШАБЛОН
  маска-включитьБуквы-исключитьБуквы
Например:
  а___н-и-ч
  В этом примере хэлпер будет искать слова длиной 5 символов, где на первом месте
  стоит А, на последнем Н, причем в слове должны быть буква И, и не должно быль буквы Ч
  
  Если вам не нужно включать/исключать буквы, ничего не оставляйте между "-" ничего.
  ан__ас--
  а__нас-а-''')
    lastwds = []
    a = input('>')
    while a:
        if a == '*':
            print('\n'.join(lastwds))
        elif a.count('-') != 2:
            print('2x"-" expected')
        else:
            mask, inc, exc = a.split('-')
            wds = guess(mask, inc, exc)
            if not wds:
                print('Can\'t find words that match')
            else:
                lastwds = wds.copy()
                b = wds.copy()
                random.shuffle(b)
                print(', '.join(b[:min(len(b), 5)]))
                if len(wds) > 5:
                    print('...  Type "*" to see all variants')
        a = input('>')
