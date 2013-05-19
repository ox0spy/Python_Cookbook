#!/usr/bin/env python
# -*- coding: utf-8 -*-
import itertools
import os


def anyTrue(predicate, sequence):
    return True in itertools.imap(predicate, sequence)


def endsWith(s, *endings):
    return anyTrue(s.endswith, endings)


if __name__ == '__main__':
    for f in os.listdir('.'):
        if endsWith(f, '.jpg', '.jpeg', '.gif'):
            print f
