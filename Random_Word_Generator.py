import random

import linecache

def random_word():
    n = random.randint(1,5449)
    w = linecache.getline('WORDS.txt',n)
    return w
# 5449 lines in text file WORDS.txt, each containing an English word
# linecache.getline(<filename>,<line no.>) returns content of the specified line


def letters():
    l=[]
    for i in random_word():
        l.append(i.upper())
    l.pop()
    return l
