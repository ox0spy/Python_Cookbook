#!/usr/bin/env python
# -*- coding: utf-8 -*-
import string


allchars = string.maketrans('', '')


def makefilter(s, keep):
    delchars = allchars.translate(allchars, keep)
    return s.translate(allchars, delchars)


if __name__ == '__main__':
    keep = 'aeiouy'
    print makefilter('four score and seven years ago', keep)
    print makefilter('tiger, tiger burning bright', keep)
