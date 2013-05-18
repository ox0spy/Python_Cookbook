#!/usr/bin/env python
#-*- coding: utf-8 -*-
import string


def translator(frm='', to='', delete='', keep=None):
    if len(to) == 1:
        to = to * len(frm)
    trans = string.maketrans(frm, to)
    if keep is not None:
        allchars = string.maketrans('', '')
        delete = allchars.translate(allchars,
                                    keep.translate(allchars, delete))

    def translate(s):
        return s.translate(trans, delete)

    return translate


def main():
    s ='Chris Perkins : 224-7992'
    print 'string s:', s

    digits_only = translator(keep=string.digits)
    print 'digits_only:', digits_only(s)

    no_digits = translator(delete=string.digits)
    print 'no_digits:', no_digits(s)

    digits_to_hash = translator(frm=string.digits, to='#')
    print 'digits_to_hash:', digits_to_hash(s)


if __name__ == '__main__':
    main()
