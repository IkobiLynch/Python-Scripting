#!/usr/bin/env python3

# Counts all characters in a string and outputs it

import argparse

parser = argparse.ArgumentParser(
        prog='Count all charactes',
        description='Counts all characters in a string and outputs it'
        )
parser.add_argument('string', help='input string')

args = parser.parse_args().string

dictio = {}
for letter in args:
    if letter in dictio:
        dictio[letter] += 1
    else:
        dictio[letter] = int(1)

print(dictio)
