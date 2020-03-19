from __future__ import unicode_literals
# $Id$
# $Revision$
#
#    libsnmp - a Python SNMP library
#    Copyright (c) 2003 Justin Warren <daedalus@eigenmagic.com>
# 
# Some utility functions to help make life easier

from builtins import oct
from builtins import bytes
import sys

def _b(obj):
    if sys.version_info[0] < 3:
        return bytes(obj, 'latin1')
    else:
        return obj

def join_b(list_of_bytes):

    """ join list of newbytes (<3) or bytes and return newbytes or bytes object """
    if sys.version_info[0] < 3:
        return bytes(b''.join(list_of_bytes), 'latin1')
    else:
        return b''.join(list_of_bytes)

def octetsToHex(octets):
    """ convert a string of octets to a string of hex digits
    """
    result = ''
    while octets:
        byte = octets[0]
        octets = octets[1:]
        result += "%.2x" % byte

    return result

def octetsToOct(octets):
    """ convert a string of octets to a string of octal digits
    """
    result = ''
    while octets:
        byte = octets[0]
        octets = octets[1:]
        result += "%.4s," % oct(byte)
    return result

