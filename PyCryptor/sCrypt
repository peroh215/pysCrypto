#!/usr/bin/env python
#-*- coding: utf-8 -*-

# Imports
import random
import sys

# Functions
def define_alphanum():
    alphanum = 'aAbBcCdDeEfFgGhHiIjJkKlLmMnNoOpPqQrRsStTuUvVwWxXyYzZ1234567890!?@#$%&^;âàáêèéîìíôòóûùú'
    return alphanum

def encrypt(string, key):
    alphanum = define_alphanum()
    encrypted = ''
    for char in string:
        if char in alphanum:
            try:
                pos = alphanum.find(char)
                newPos = (pos + key) % 87
                newChar = alphanum[newPos]
                encrypted += newChar
            except IndexError as ie:
                print('ERROR: Key is too big ({})'.format(ie))
        elif char == ' ':
            encrypted += ' '
        else:
            encrypted += char
    return encrypted

def decrypt(string, key):
    alphanum = define_alphanum()
    for char in string:
        if char in alphanum:
            pos = alphanum.find(char)
            oldPos = (pos - key) % 72
            oldChar = alphanum[oldPos]
            decrypted += oldChar
        elif char == ' ':
            decrypted += ' '
        else:
            decrypted += char
