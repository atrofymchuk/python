#!/bin/python3
"""
This script gets system information like distro info, memory(total, used, free)
CPU info (model, core numbers, speed), current user, system load average
IP address. Use params for specifying resource. (e.g. -d for distro
-m for memory, -c for CPU, -u for user info, -l for load average
-i for IP address).
"""
import subprocess
import argparse


def main():
    """
    This script gets system information like distro info, memory(total, used, free)
    CPU info (model, core numbers, speed), current user, system load average
    IP address. Use params for specifying resource. (e.g. -d for distro
    -m for memory, -c for CPU, -u for user info, -l for load average
    -i for IP address).
    """
    parser = argparse.ArgumentParser(description='gets system information')
    parser.add_argument('-d', dest='distro', action='store_true',
                        help="gets system information like distro info")
    parser.add_argument('-m', dest='memory', action='store_true',
                        help="gets memory(total, used, free)")
    parser.add_argument('-c', dest='cpu', action='store_true',
                        help="gets info about CPU")
    parser.add_argument('-u', dest='user', action='store_true',
                        help="gets info about user")
    parser.add_argument('-l', dest='load_aver', action='store_true',
                        help="gets info about load average")
    parser.add_argument('-i', dest='ip_address', action='store_true',
                        help="gets info  IP address")
    args = parser.parse_args()

    if args.distro:
        subprocess.run(['lsb_release', '-a'], shell=False, check=True)

    if args.memory:
        subprocess.run(['free'], shell=False, check=True)

    if args.cpu:
        subprocess.run(['cat', '/proc/cpuinfo'], shell=False, check=True)

    if args.user:
        print("Current user:")
        subprocess.run(['id', '-un'], shell=False, check=True)

    if args.load_aver:
        print("Load average:")
        subprocess.run(['cat', '/proc/loadavg'], shell=False, check=True)

    if args.ip_address:
        print("IP address:")
        subprocess.run(['hostname', '-I'], shell=False, check=True)


if __name__ == "__main__":
    main()
