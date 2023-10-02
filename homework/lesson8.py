# def func_1():
#     yield 'A'
#     yield 2 + 2
#     yield 3
# # Вывести в цикле for
# for el in func_1():
#     print(el)
# # Вывести как список
# print(list(func_1()))
# # Вывести как нумерованный словарь
# print(dict(enumerate(func_1())))
# print(2 << 4)

# func_list = [lambda a, b: a + b, lambda a, b: a - b, lambda a, b: a * b]
# for func in func_list:
#     print(func(5, 2))

# list_1 = [(1, 10), (2, 3), (4, 8), (10, 1)]
# print(sorted(list_1, key=lambda a: a[1]))