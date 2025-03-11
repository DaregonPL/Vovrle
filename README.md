# Let there be Vovlre! (RUS)
Эта прога - по сути прото машина для убийства времени, копирующая другуюж немалоизвестную игру "Wordle".
Гемплей - почти такой же, поэтому убедитесь, что вы умеете играть в вордл, прежде чем попробовать мою игру, т.к. мне было лень расписывать правила.
Из основного: вам дается 6 попыток и 4 варианта сложности (чем длиннее слово, тем сложнее его угадать). Также вы можете ввести кастомную длинну слова.
### Формулы для расчета очков:

`round(wordln ** 2 / 2)` - проигрыш

`wordln ** 2 - 2` - выгирыш
### Фичи
Также в проге есть возможность выбора языка с сохранением выбора в файл, чтоб вам не пришлось каждый раз выбирать язык (помянем DungeonWord). Имеется меню настроек, которое помимо выбора 
языка предлагает сбросить игру на стройку завода или сменить имя (оно тоже хранится в файле), причем к каждому имени привязан счёт (при возвращении на старое имя вернётся старый счёт.)

## Хэлпер
Запустите helper.py и внемлите его речи

# Let there be Vovlre! (ENG)
This program is essentially a time-killing machine, copying another well-known game "Wordle".
The gameplay is almost the same, so make sure you know how to play Wordle before trying my game, because I was too lazy to describe the rules.
The main thing: you are given 6 attempts and 4 difficulty options (the longer the word, the harder it is to guess). You can also enter a custom word length.
### Formulas for calculating points:

`round(wordln ** 2 / 2)` - loss

`wordln ** 2 - 2` - win
### Features
The program also has the ability to select a language with saving the choice to a file, so you do not have to select a language every time (let's remember DungeonWord). There is a settings menu, which in addition to choosing a language
offers to reset the game to the factory construction site or change the name (it is also stored in the file), and each name is linked to an account (when returning to the old name, the old account will return.)

## Helper
Run helper.py and listen to its speech
