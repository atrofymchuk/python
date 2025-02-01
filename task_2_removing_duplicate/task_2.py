#!/usr/bin/env python3
"""
This script removes duplicate from a list and create a tuple
and find the minimum and maximum number.
"""


def main():
    """
    This function removes duplicate from a list and create a tuple
    and find the minimum and maximum number.
    """
    task_list = [1, 2, 3, 5, 4, 5, 100, 7, 8, 55, 45, 67, 5, 2, 55]
    task_list = list(set(task_list))
    task_tuple = tuple(task_list)
    print("Minimal number is:", (min(task_tuple)))
    print("Maximum number is:", (max(task_tuple)))


if __name__ == "__main__":
    main()
