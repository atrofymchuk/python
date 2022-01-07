# file_1 = open('file_1.txt', 'r')
# numbers_1 = file_1.read()
# print(file_1)
# print(numbers_1)
# file_1.close()

# file_1 = open('file_1.txt', 'r')
# print(file_1.read(3))  # Считываем первые 3 байта
# print('Current position:', file_1.tell())  # Выводим положение указателя
# file_1.seek(8)  # Смещаем указатель на 8 позицию
# print('Current position:', file_1.tell())  # Выводим положение указателя после функции seek()
# print(file_1.read(3))  # Считываем первые 3 байта от текущего положения указателя
# file_1.close()

file_1 = open('file_1.txt', 'r')
list_1 = list(file_1)
# for line in file_1:
#     list_1 = list(line)
print(list_1)