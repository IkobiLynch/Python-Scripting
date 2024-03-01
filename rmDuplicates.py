#!/usr/bin/env python3

# Script to remove duplicates from a list of given integers, create a tuple and find the min and max number.

import argparse

# Create parser
parser = argparse.ArgumentParser(
        prog="MinMax",
        description="Remove duplicates and find min max")
parser.add_argument('integers', nargs='+', type=int, help='list of integers')
args = list(parser.parse_args().integers)

# Remove duplicates and convert to tuple
no_dupe_list = list(set(args))
no_dupe_tuple = tuple(no_dupe_list)


print(f"Min: {min(no_dupe_tuple)} \nMax: {max(no_dupe_tuple)} ")

