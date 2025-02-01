#!/usr/bin/env python3
"""
This script reads access log from file (name of file is provided as argument).
As output script provides total number of different User Agents and than provides
statistic with number of requests from each of them.
"""
import argparse
from collections import Counter


def main():
    """
    This function reads access log from file (name of file is provided as argument).
    As output script provides total number of different User Agents and than provides
    statistic with number of requests from each of them.
    """
    parser = argparse.ArgumentParser(description='read file')
    parser.add_argument('filename')
    args = parser.parse_args()

    with open(args.filename, 'r', encoding='utf-8') as file:
        i = 1
        list_2 = []
        list_3 = []
        for line in file:
            list_1 = line.split()
            how_long = len(list_1)
            if how_long > 12:
                if list_1[11] == 'union':
                    list_2 = " ".join(list_1[14:])
                    list_3.append(list_2)
                else:
                    list_2 = " ".join(list_1[11:])
                    list_3.append(list_2)
            i = i + 1

    dict_1 = Counter(list_3)
    dict_2 = {d: dict_1[d] for d in sorted(dict_1, key=dict_1.get, reverse=True)}

    print("Total number of different User Agents:", len(dict_2.keys()))
    print(" Value        User agent")

    for key, value in dict_2.items():
        print(f" {key}  {value}")


if __name__ == "__main__":
    main()
