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

# file_1 = open('file_1.txt', 'r')
# list_1 = list(file_1)
# # for line in file_1:
# #     list_1 = list(line)
# print(list_1)

# file_1 = open('file_2.txt', 'w')
# file_1.write('four words\ntwo strings')
# file_1.close()

veg = {
    "помидор": {
        "id": 1,
        "пищевая ценность": {
            "белки": 1.1,
            "жиры": 0.2,
            "углеводы": 3.8,
            "калорийность": 24
        },
        "блюда": [
            "лазанья",
            "борщ",
            "пицца"
        ]
    },
    "картофель": {
        "id": 2,
        "пищевая ценность": {
            "белки": 2,
            "жиры": 0.1,
            "углеводы": 17,
            "калорийность": 77
        },
        "блюда": [
            "борщ",
            "зразы",
            "испанская тортилья"
        ]
    },
    "петрушка": {
        "id": 3,
        "пищевая ценность": {
            "белки": 3,
            "жиры": 0.8,
            "углеводы": 6,
            "калорийность": 36
        },
        "блюда": [
            "аджика",
            "борщ",
            "рулет"
        ]
    }
}

with open('file_3.txt', 'w', encoding='cp1251') as file_1:
     file_1.write(str(veg))

with open('file_6.txt', 'r', encoding='cp1251') as file_1:
    exec('veg = ' + file_1.read())
print(veg['помидор']['блюда'])