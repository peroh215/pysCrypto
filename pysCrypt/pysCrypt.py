#!/usr/bin/env python
#-*- coding: utf-8 -*-

__author__ = 'Blackman White'

# Imports
import random
import sys
import math

# Functions
def define_alphanum():
    alphanum = 'aAbBcCdDeEfFgGhHiIjJkKlLmMnNoOpPqQrRsStTuUvVwWxXyYzZ1234567890!?@#$%&^*¨+-;âàáêèéîìíôòóûùú'
    return alphanum

def define_num():
    numbers = '1234567890'
    return numbers

def encrypt(string, key,debug=0):
    alphanum = define_alphanum()
    encrypted = ''
    for char in string:
        if char in alphanum:
            try:
                pos = alphanum.find(char)
                if debug == 1:
                    print('pos:',pos)
                newPos = int((pos + key * math.pi + 1 * math.e * math.tau * 2 + 1) % 90)
                if debug == 1:
                    print(newPos)
                newChar = alphanum[newPos]
                encrypted += newChar
            except IndexError as ie:
                print('ERROR: Key is too big ({})'.format(ie))
        elif char == ' ':
            encrypted += ' '
        else:
            encrypted += char
    return encrypted

def secure_encrypt(string, key, debug=0):
    alphanum = define_alphanum()
    encrypted = ''
    for char in string:
        if char in alphanum:
            try:
                pos = alphanum.find(char)
                if debug == 1:
                    print('pos:',pos)
                newPos = int((pos + key * (math.pi + 1) * math.e * math.tau * 2 + (6 * 1024 * 2) * 524 + 6754 * 17291 * 32 + 1 * 9 * 2 * 4 * 8 * 16 + 53235231296413 * 2 + 1 * 124 + (math.e * 100) * math.pi * 2 + 5 * 420 + 69 * 912 + 7542 + math.tau * math.e * 2048 + 1928 * 666) % 90)
                if debug == 1:
                    print(newPos)
                newChar = alphanum[newPos]
                encrypted += newChar
            except IndexError as ie:
                print('ERROR: Key is too big ({})'.format(ie))
            except OverflowError as oe:
                print('FATAL ERROR: Overflow ({})'.format(oe))
        elif char == ' ':
            encrypted += ' '
        else:
            encrypted += char
    return encrypted

def simple_encrypt(string, key, debug = 0):
    alphanum = define_alphanum()
    encrypted = ''
    for char in string:
        if char in alphanum:
            try:
                pos = alphanum.find(char)
                if debug == 1:
                    print('pos:',pos)
                newPos = int((pos + key) % 90)
                if debug == 1:
                    print(newPos)
                newChar = alphanum[newPos]
                encrypted += newChar
            except IndexError as ie:
                print('ERROR: Key is too big ({})'.format(ie))
        elif char == ' ':
            encrypted += ' '
        else:
            encrypted += char
    return encrypted    

def decrypt(string, key, debug=0):
    decrypted = ''
    alphanum = define_alphanum()
    for char in string:
        if char in alphanum:
            pos = alphanum.find(char)
            if debug == 1:
                print('pos:',pos)
            oldPos = int((pos - key / math.pi + 1 / math.e / math.tau / 2 - 37) % 90)
            if debug == 1:
                print(oldPos)
            oldChar = alphanum[oldPos]
            decrypted += oldChar
        elif char == ' ':
            decrypted += ' '
        else:
            decrypted += char
    return decrypted

def simple_decrypt(string, key, debug=0):
    decrypted = ''
    alphanum = define_alphanum()
    for char in string:
        if char in alphanum:
            pos = alphanum.find(char)
            if debug == 1:
                print('pos:',pos)
            oldPos = int((pos - key) % 90)
            if debug == 1:
                print(oldPos)
            oldChar = alphanum[oldPos]
            decrypted += oldChar
        elif char == ' ':
            decrypted += ' '
        else:
            decrypted += char
    return decrypted

def secure_decrypt(string, key, debug=0):
    decrypted = ''
    alphanum = define_alphanum()
    for char in string:
        if char in alphanum:
            pos = alphanum.find(char)
            if debug == 1:
                print('pos:',pos)
            oldPos = int((pos - key / (math.pi + 1) / math.e / math.tau / 2 - (6 / 1024 / 2) / 524 - 6754 / 17291 / 32 - 1 / 9 / 2 / 4 / 8 / 16 - 53235231296413 / 2 - 1 / 124 - (math.e / 100) / math.pi / 2 - 5 / 420 - 69 / 912 - 7542 - math.tau / math.e / 2048 - 1928 / 666 - 73) % 90)
            if debug == 1:
                print(oldPos)
            oldChar = alphanum[oldPos]
            decrypted += oldChar
        elif char == ' ':
            decrypted += ' '
        else:
            decrypted += char
    return decrypted
