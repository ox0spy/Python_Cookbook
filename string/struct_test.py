#!/usr/bin/env python
# -*- coding: utf-8 -*-
import struct
import binascii
import ctypes


def test():
    values = (123, 'abc', 3.14)
    s = struct.Struct('I3sf')
    packed_data = s.pack(*values)
    unpacked_data = s.unpack(packed_data)

    print 'values:', values
    print 'format string:', s.format
    print 's.size:', s.size  # 'I3sf' - 4+3*1+4+1
    print 'packed_data:', packed_data
    print 'unpacked_data:', unpacked_data


def test_pack_into():
    values = (123, 'abc', 3.14)
    s = struct.Struct('I3sf')
    prebuf = ctypes.create_string_buffer(s.size)
    print 'before pack_into:', binascii.hexlify(prebuf)
    s.pack_into(prebuf, 0, *values)
    print 'after pack_into:', binascii.hexlify(prebuf)
    unpacked_data = s.unpack_from(prebuf, 0)
    print 'after unpack_from:', unpacked_data


def test_pack_into2():
    v1 = (123, 'abc', 3.14)
    v2 = (888, 'bird')
    s1 = struct.Struct('I3sf')
    s2 = struct.Struct('I4s')

    buf = ctypes.create_string_buffer(s1.size + s2.size)
    print 'before:', binascii.hexlify(buf)
    s1.pack_into(buf, 0, *v1)
    s2.pack_into(buf, s1.size, *v2)
    print 'after pack:', binascii.hexlify(buf)
    print s1.unpack_from(buf, 0)
    print s2.unpack_from(buf, s1.size)

if __name__ == '__main__':
    print 'function test'
    test()

    print
    print 'function test_pack_info'
    test_pack_into()

    print
    print 'function test_pack_info'
    test_pack_into()
