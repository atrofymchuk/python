#!/usr/bin/env python3
"""
    This script accepts file name and puts extension to output.
    If there is no extension - exception raise.
"""
import argparse


def main():
    """
    This function accepts file name and puts extension to output.
    If there is no extension - exception raise.
    """
    parser = argparse.ArgumentParser(description='Script reads file')
    parser.add_argument('filename', help="Name of file")
    args = parser.parse_args()
    file_name = args.filename.split(".")
    length_extension = len(file_name[-1])
    if length_extension > 3 or length_extension < 1:
        raise Exception("Sorry, file doesn't have extension!")
    print(file_name[-1])


if __name__ == "__main__":
    main()
