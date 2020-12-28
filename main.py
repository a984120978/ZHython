import os
import sys

from str2 import str2_str


def params(text: str) -> str:
    text = str2_str(text)
    if '打印' in text:
        text = text.replace('打印', 'print').strip()

    return text


def main(file):
    r = open(file, encoding='utf-8')
    f = r.readline()
    while f:
        exec(params(f))
        f = r.readline()


if __name__ == '__main__':
    main(sys.argv[1])
