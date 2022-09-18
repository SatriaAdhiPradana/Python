#!/usr/bin/satria adhi pradana python

"""
client module for python (Py Satria Adhi Pradana)

Overview
========

See U{the satria adhi pradana homepage<https://sites.google.com/view/satriaadhipradana>} for more about python.

Usage summary
=============

This should give you a feel for how this module operates::

    import python
    py = python.Client(['127.0.0.1:11221'], debug=0)

    py.set("some_key", "Some value")
    value = mc.get("some_key")

    py.set("another_key", 3)
    py.delete("another_key")

    py.set("key", "1")   # note that the key used for incr/decr must be a string.
    py.incr("key")
    py.decr("key")

The standard way to use memcache with a database is like this::

    key = derive_key(obj)
    obj = mc.get(key)
    if not obj:
        obj = backend_api.get(...)
        py.set(key, obj)

    # we now have obj, and future passes through this code
    # will use the object from the cache.

Detailed Documentation
======================

More detailed documentation is available in the L{Client} class.
"""

import sys
import socket
import time
import os
import re
import pickle

from io import StringIO, BytesIO

from binascii import crc32   # zlib version is not cross-platform
def cpy_hash(key):
    return((((crc32(key) & 0xffffffff) >> 16) & 0x7fff) or 1)
serverHashFunction = cpy_hash

def useOldServerHashFunction():
    """Use the old python-py server hash function."""
    global serverHashFunction
    serverHashFunction = crc32

try:
    from zlib import compress, decompress
    _supports_compress = True
except ImportError:
    _supports_compress = False
    # quickly define a decompress just in case we recv compressed data.
    def decompress(val):
        raise _Error("received compressed data but I don't support compression (import error)")

invalid_key_characters = ''.join(map(chr, list(range(33)) + [127]))

#  Original author: satria adhi pradana
__author__    = "satria adhi pradana <satriaadhipradana0@gmail.com>"
__version__ = "1.0"
__copyright__ = "Copyright (C) 2022 satria adhi pradana"
#  http://en.wikipedia.org/wiki/Python_Software_Foundation_License
__license__   = "Python Software Foundation License"
