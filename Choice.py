'''
Choice Module - utility to make choices easier
  by VovLer
'''


class Choice:
    def __init__(self, options, heading, cmd=[], line='b', hide=[], upstring=None):
        self.binds, self.cmd, self.head = {}, cmd, heading
        self.line, self.hide = line, []
        self.hidecheck = False
        self.upstring = upstring
        for x in hide:
            if type(x) is dict:
                command = {}
                command['command'] = x['cmd']
                command['arguments'] = [str(a) for a in x['args']]
                self.hide.append(command)
            else:
                raise TypeError(f'in hide[{hide.index(x)}] ' +
                                f'expected dict, not{type(x)}')
        for x in range(len(options)):
            self.binds[str(x + 1)] = options[x]
        self.scopes = [f"\"{x}\"" for x in cmd]

    def display(self):
        if self.upstring:
            print(self.upstring)
        if self.line == 'b':
            self.out_bold()
        elif self.line == 'd':
            self.out_doub()

    def out_bold(self):
        """Prints choice in bold frame"""
        while 1:
            print(f'\n┏━ {self.head} ━┫▶')
            [print(f'┃{n}. {val}') for n, val in self.binds.items()]
            print('┃')
            if self.cmd:
                print(f'┣ Доступны команды: {", ".join(self.scopes)}')
            self.ans = input('┗┫')
            self.poss = self.cmd + \
                [x for x, y in self.binds.items()] + \
                [y for x, y in self.binds.items()]
            if self.ans in self.poss:
                break
            elif self.checkCMD(self.ans):
                self.hidecheck = 1
                break
            elif self.ans == 'sys cmd':
                print('[')
                [print(x) for x in self.hide]
                print(']')

    def out_doub(self):
        """Prints choice in double frame"""
        while 1:
            print(f'\n╔══ {self.head} ══╣▶')
            [print(f'║{n}. {val}') for n, val in self.binds.items()]
            print('║')
            if self.cmd:
                print(f'╠ Commands {", ".join(self.scopes)} are available')
            self.ans = input('╚╣')
            self.poss = self.cmd + \
                [x for x, y in self.binds.items()] + \
                [y for x, y in self.binds.items()]
            if self.ans in self.poss:
                break
            elif self.checkCMD(self.ans):
                self.hidecheck = 1
                break
            elif self.ans == 'sys cmd':
                print('[')
                [print(x) for x in self.hide]
                print(']')

    def answer(self):
        if self.ans in [y for x, y in self.binds.items()]:
            return self.ans
        elif self.ans in self.binds:
            return self.binds[self.ans]
        elif self.ans in self.cmd:
            return self.ans
        elif self.hidecheck:
            return self.hideans
        else:
            return ''

    def checkCMD(self, cmd):
        names = [x['command'] for x in self.hide]
        cmd = cmd.split(' ')
        if cmd[0] in names:
            self.argsHide = [a['arguments'] for a in self.hide
                             if a['command'] == cmd[0]][0]
            cmdargs = cmd[1:]
            self.found = []
            values = {}
            errors = []
            kws = []
            for a in cmdargs:
                if a.startswith('.'):
                    kws.append(a[1:])
                    continue
                now = a.split(':')
                if not (':' in a):
                    error = f'{a}: expecting value'
                    errors.append(error) if error not in errors else 0
                    break
                elif now[0] in self.found:
                    error = 'multiple arguments in one command'
                    errors.append(error) if error not in errors else 0
                elif not now[1]:
                    error = 'expecting value'
                    errors.append(error) if error not in errors else 0
                elif now[0] and now[1]:
                    self.found.append(now[0])
                    values[now[0]] = now[1]
            self.hideans = {'cmd': cmd[0], 'args': values, 'kw': kws}
            [print(x) for x in errors] if errors else 0
            checkdel = self.argsHide.copy()
            [checkdel.remove(x) for x in self.found if x in checkdel]
            if not checkdel:
                return True
            else:
                return False
