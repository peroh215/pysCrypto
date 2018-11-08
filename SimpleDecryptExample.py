#!/usr/bin/env python
#-*- coding: utf-8 -*-

from sCrypt import sCrypt

cyph = sCrypt.encrypt('Hello', 2525)
print(cyph)
print(sCrypt.decrypt(cyph, 2525))
