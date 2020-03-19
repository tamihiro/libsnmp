## Little note about my fork
Been a long time user of the original [jpwarren/libsnmp](https://github.com/jpwarren/libsnmp) with much appreciation because PySNMP was, and still is as of this writing, way too slow to be used in my app. 

Now I need to make my app run with Python 3, I've forked his repo and made minimum necessary changes to files in `test/` and `lib/libsnmp/` directories so the module works with both Python 2.7 and 3.x.

The changes result in the relevant part of my app being about 1.18 times slower than before, while still much faster (about 17.6 times) than with PySNMP. 

(original README follows)

# libsnmp
A pure Python SNMP library

## Overview

I wrote this library many years ago because I was frustrated by PySNMP and something else that
I can't recall, but that used an overly theoretical CompSci-type implementation of ASN.1 entities mapped
directed to a deep class hierarchy, which made it really slow.

The PySNMP project has now utterly eclipsed the functionality of libsnmp, so you probably want to use it instead.

The code is here mostly for historical reference, and so people who keep downloading it from PyPI for some
unknown reasons can fork and update the code if they so wish.

## Installation
libsnmp is available in PyPI, so you can just use:

```
pip install libsnmp
```
if you want. Or use:

```
python setup.py install
```

There are a bunch of example scripts in the main directory.
