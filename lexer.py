from io import TextIOWrapper


class LexerTS:
    file: TextIOWrapper

    def __init__(self, file):
        self.file = file
        self.line = 0
        self.c = ''

    def nextc(self):
        self.c = self.file.read(1)
        if self.c == '\n':
            self.line += 1
        return self.c

    def prevseek(self):
        if self.c == '\n':
            self.line -= 1
        pos = self.file.tell() - 1
        self.file.seek(pos, 0)
        return pos

    def getToken(self):
        pass

    def dropToken(self):
        self.skipwspace()
        c = self.nextc()
        self.prevseek()

        if c.isalnum():
            return self.iden()
        if c.isnumeric():
            return self.num()
        else:
            return self.special()

    def comment(self):
        pass

    def skipwspace(self):
        c = ' '
        while c.isspace():
            c = self.nextc()

        if not c == '':
            self.prevseek()

    def iden(self):
        c = self.nextc()
        t = ''
        while c.isalpha() or c.isnumeric():
            t += c
            c = self.nextc()

        if t:
            self.prevseek()

        return t

    def num(self):
        pass

    def special(self):
        c = self.nextc()

        # if c in [':','(',')','{']:
        #     return c

        if c == '-':
            t = c
            c = self.nextc()
            if c == '>':
                t += c
            else:
                self.prevseek()

            return t
        if c == '{':
            return c
        if c == '(':
            return c
        if c == ')':
            return c
        if c == ':':
            return c

        return None
