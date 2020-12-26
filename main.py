import os
import sys


def params(text: str):
    text = text.replace('（', '(').replace('）', ')').replace('“', '"').replace('”', '"')
    if '打印' in text:
        text = text.replace('打印', 'print')
        exec(text)


if __name__ == '__main__':
    r = open(sys.argv[1], encoding='utf-8')
    f = r.readline()
    while f:
        params(text=f)
        f = r.readline()
