#!/usr/bin/env python3
"""
This script uses packages stored in the cache, takes these packages from cache and then puts them
to Gitlab Package Registry
"""

import os

os.system('pip cache list --format=abspath > packages.txt')
with open("packages.txt", 'r', encoding='utf-8') as file:
    lines = file.readlines()
    i = 0
    list_packages = []
    for line in lines:
        list_name_package = lines[i]
        STR_LIST_NAME_PACKAGE = str(list_name_package)
        NAME_PACKAGE = STR_LIST_NAME_PACKAGE.rstrip()
        list_packages.append(NAME_PACKAGE)
        i += 1
for name in list_packages:
    os.system(f'python3 -m twine upload --repository gitlab {name}')
