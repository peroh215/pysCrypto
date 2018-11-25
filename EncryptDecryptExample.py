#!/usr/bin/env python
#-*- coding: utf-8 -*-

from pysCrypt import pysCrypt

msg = 'Hello world!'

cyph = pysCrypt.encrypt(msg, 256)
s_cyph = pysCrypt.simple_encrypt(msg, 256)
se_cyph = pysCrypt.secure_encrypt(msg, 256)
print(cyph + '\n' + s_cyph + '\n' + se_cyph)

print('\nDecrypt:', pysCrypt.decrypt(cyph, 256))
print('Simple decrypt:', pysCrypt.simple_decrypt(s_cyph, 256))
print('Secure decrypt:' , pysCrypt.secure_decrypt(se_cyph, 256))
