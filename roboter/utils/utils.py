#!/usr/bin/env python3

import sys
import unicodedata

def unicode_to_ascii(res):
    return unicodedata.normalize('NFKC', res)

# print(unicode_to_ascii("ｎ"))

if __name__ == '__main__':
    sys.exit(0)

