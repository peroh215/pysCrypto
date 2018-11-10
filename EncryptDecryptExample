#!/usr/bin/env python
#-*- coding: utf-8 -*-

from pysCrypt import pysCrypt

msg = 'Hello world!'

cyph = sCrypt.encrypt(msg, 256)
s_cyph = sCrypt.simple_encrypt(msg, 256)
se_cyph = sCrypt.secure_encrypt(msg, 256)
print(cyph + '\n' + s_cyph + '\n' + se_cyph)

print('\nDecrypt:', sCrypt.decrypt(cyph, 256))
print('Simple decrypt:', sCrypt.simple_decrypt(s_cyph, 256))
print('Secure decrypt:' , sCrypt.secure_decrypt(se_cyph, 256))
