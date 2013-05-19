#!/usr/bin/env python
# -*- coding: utf-8 -*-
import re


def multiple_replace(s, adict):
    rx = re.compile('|'.join(map(re.escape, adict)))

    def one_xlat(match):
        return adict[match.group(0)]

    return rx.sub(one_xlat, s)


def make_xlat(*args, **kwds):
    adict = dict(*args, **kwds)
    rx = re.compile('|'.join(map(re.escape, adict)))
    # rx = re.compile(r'\b%s\b' % r'\b|\b'.join(map(re.escape, adict)))

    def one_xlat(match):
        return adict[match.group(0)]

    def xlat(s):
        return rx.sub(one_xlat, s)

    return xlat


class MakeXlat():
    def __init__(self, *args, **kwds):
        self.adict = dict(*args, **kwds)
        self.rx = self.make_rx()

    def make_rx(self):
        return re.compile('|'.join(map(re.escape, self.adict)))

    def one_xlat(self, match):
        return self.adict[match.group(0)]

    def __call__(self, s):
        return self.rx.sub(self.one_xlat, s)


def main():
    s = 'hello, world'
    adict = {'hello': 'hi', 'world': 'master'}

    print 'test', multiple_replace.__name__
    print 's: %s' % s
    print multiple_replace(s, adict)

    s = 'Larry Wall is the creator of Perl'
    adict = {'Larry Wall': 'Guido van Rossum',
             'creator': 'Benevolent Dictator for Life',
             'Perl': 'Python',
             }

    print
    print 's:', s
    print
    print 'test', multiple_replace.__name__
    print multiple_replace(s, adict)

    print
    print 'test', make_xlat.__name__
    translate = make_xlat(adict)
    print translate(s)

    print
    print 'test', MakeXlat.__name__
    m = MakeXlat(adict)
    print m(s)

    class make_xlat_by_whole_words(MakeXlat):
        def make_rx(self):
            return re.compile(r'\b%s\b' % r'\b|\b'.join(map(re.escape,
                                                            self.adict)))

    print
    print 'test', make_xlat_by_whole_words.__name__
    mx = make_xlat_by_whole_words(adict)
    print mx(s)

if __name__ == '__main__':
    main()
