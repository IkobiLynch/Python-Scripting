#!/usr/bin/env python3

# Gets system information.

import argparse
import platform
import psutil
import socket
import sys

# Function Definitions - start
def get_distro_info():
    return platform.dist()

def get_memory_info():
    memory = psutil.virtual_memory()
    total = memory.total
    used = memory.used
    free = memory.free
    return total, used, free

def get_cpu_info():
    cpu_info = {}
    cpu_info['model'] = platform.processor()
    cpu_info['cores'] = psutil.cpu_count(logical=False)
    cpu_info['speed'] = psutil.cpu_freq().current
    return cpu_info

def get_current_user():
    return psutil.users()[0].name

def get_load_average():
    return psutil.getloadavg()

def get_ip_address():
    return socket.gethostbyname(socket.gethostname())

# Function Definitions - end

# Create parser

parser = argparse.ArgumentParser(
        prog='Get system Info',
        description='Gets various system information depending on the flag passed to the script.'
        )
parser.add_argument('-d', '--distro', action='store_true', help='Show distro info')
parser.add_argument('-m', '--memory', action='store_true', help='Show total, used, free memory')
parser.add_argument('-c', '--cpu', action='store_true', help='Show model, core numbers, speed')
parser.add_argument('-u', '--user', action='store_true', help='Show user info')
parser.add_argument('-l', '--load', action='store_true', help='Show load average')
parser.add_argument('-i', '--ip', action='store_true', help='Show IP Address')

args = parser.parse_args()

if not any(vars(args).values()):
    print("No argument provided to command. Run <command> --help for more info")
    sys.exit(1)

# Decides output based on the arguments passed when script is ran

if args.distro:
    print("Distro Info:", get_distro_info())

if args.memory:
    total, used, free = get_memory_info()
    print("Memory Info - Total:", total, "bytes, Used:", used, "bytes, Free:", free, "bytes")

if args.cpu:
    cpu_info = get_cpu_info()
    print("CPU Info -  Model:", cpu_info['model'], ", Cores:", cpu_info['cores'], ", Speed:", cpu_info['speed'], "MHz")

if args.user:
    print(f"Current user: {get_current_user()}")

if args.load:
    print("System Load Average:", get_load_average())

if args.ip:
    print("IP Address:", get_ip_address())




