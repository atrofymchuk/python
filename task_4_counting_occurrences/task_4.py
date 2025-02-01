#!/usr/bin/env python3
"""
This script gets string, count occurrences of all characters within a string
(e.g. pythonnohtyppy -> p:3, y:3, t:2, h:2, o:2, n:2)
"""
import argparse
from collections import Counter


def main():
    """
    This function gets string, count occurrences of all characters within a string
    (e.g. pythonnohtyppy -> p:3, y:3, t:2, h:2, o:2, n:2)
    """
    parser = argparse.ArgumentParser(description='Script reads string')
    parser.add_argument('string', help="Input string")
    args = parser.parse_args()
    list_1 = list(args.string)
    dict_1 = Counter(list_1)
    dict_2 = {d: dict_1[d] for d in sorted(dict_1, key=dict_1.get, reverse=True)}
    print("".join([f"{x}:{y}," for x, y in dict_2.items()]))


if __name__ == "__main__":
    main()
