#!/usr/bin/env python
#-*- coding: utf-8 -*-

from pysCrypto import pysCrypto

msg = 'Hello world!'

cyph = pysCrypto.encrypt(msg, 256)
s_cyph = pysCrypto.simple_encrypt(msg, 256)
se_cyph = pysCrypto.secure_encrypt(msg, 256)
print(cyph + '\n' + s_cyph + '\n' + se_cyph)

print('\nDecrypt:', pysCrypto.decrypt(cyph, 256))
print('Simple decrypt:', pysCrypto.simple_decrypt(s_cyph, 256))
print('Secure decrypt:' , pysCrypto.secure_decrypt(se_cyph, 256))
