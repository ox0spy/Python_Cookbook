#!/usr/bin/env python
# -*- coding: utf-8 -*-
import struct


def fields(fmt, s, lastfield=False):
    numremain = len(s) - struct.calcsize(fmt)
    fmt = '%s %d%s' % (fmt, numremain, lastfield and 's' or 'x')
    return struct.unpack(fmt, s)


# test memoizing
def new_fields(fmt, s, lastfield=False, _cache={}):
    key = fmt, len(s), lastfield
    format = _cache.get(key)
    if not format:
        numremain = len(s) - struct.calcsize(fmt)
        _cache[key] = format = "%s %d%s" % \
                (fmt, numremain, lastfield and 's' or 'x')
    return struct.unpack(format, s)


if __name__ == '__main__':
    s = 'appleabcorangebanana'
    fmt = '5s 3x 6s 6s'
    print fields(fmt, s)
