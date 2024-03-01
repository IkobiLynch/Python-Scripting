#!/usr/bin/env python3

import argparse

parser = argparse.ArgumentParser(
        prog='Extention',
        description='Returns the extension of a source file')
parser.add_argument('filename', help='Name of source file')

try:
    args = parser.parse_args().filename.split('.')
    extension = args[1]
    print(extension)
except IndexError as e:
    print("Error: File has no extension, check filename entered.")

except Exception as ex:
    print(f"Error: {ex}")


