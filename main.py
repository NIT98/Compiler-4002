import os
from posixpath import abspath
import sys

from lexer import LexerTS


if len(sys.argv) < 2:
    print("please enter file address.")
    exit(1)

path = abspath(sys.argv[1])

if not os.path.isfile(path):
    print("file addres incorrect.")
    exit(1)

file = open(path)
lexer = LexerTS(file)
while True:
    token = lexer.dropToken()
    if not token:
        break
    print(token)
