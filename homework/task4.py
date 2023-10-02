list = [
    {'total': 999641890816, 'used': 228013805568},
    {'total': 61686008768, 'used': 52522710872},
    {'total': 149023482194, 'used': 83612310700},
    {'total': 498830397039, 'used': 459995976927},
    {'total': 93386008768, 'used': 65371350065},
    {'total': 988242468378, 'used': 892424683789},
    {'total': 49705846287, 'used': 9522710872},
]
number = int(input("Введите номер накопителя:")) - 1
free_mem_number = (list[number]['total']) - (list[number]['used'])
free_mem_percent = 100 - (list[number]['used']) * 100 / (list[number]['total'])
free_mem_number1 = (round(free_mem_number*1e-09))
free_mem_percent1 = (round(free_mem_percent))
if free_mem_number1 < 10 or free_mem_percent1 < 5:
    print(f'на накопителе {number + 1} критически мало свободного места')
elif free_mem_number1 > 10 and free_mem_number1 < 30 or free_mem_percent1 > 5 and free_mem_percent1 < 10:
    print(f'на накопителе {number + 1} мало свободного места')
else: print(f'на накопителе {number +1} достаточно свободного места')