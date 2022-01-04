list_1 = [11, 10, 92, 4, 10, 'str1', [76, 'Bobby']]
list_2 = ['str2', 45]
print(list_1[2]) # Элемент по индексу
print(list_1[4:]) # Срез
print(list_1 + list_2) # Конкатенация
print(list_2*3) # Дублирование
print(len(list_1)) # Длина списка
print(list_1.index('str1')) # Индекс указанного элемента
list_3 = [4, 10, 'str1', [76, 'Bobby']]
list_3.append(901) # Добавить элемент в конец списка
print(list_3)
list_3.insert(1, 'tree') # Добавляет элемент на указанную позицию
print(list_3)
list_3.extend(['M', 15.2]) # Добавить элементы последовательности в конец списка
print(list_3)
list_3.pop(3) # Удалить элемент с указанным индексом
print(list_3)
list_3.remove([76, 'Bobby']) # Удалить элемент с указанным значением
print(list_3)
list_3.reverse() # Реверс списка
print(list_3)

list_4 = [4, 10, 'str1', [76, 'Bobby']]
print(list_4.append(23))
print(list_4)

list_5 = [4, 10, 'str1', [76, 'Bobby']]
list_5 = list_5.append(23) # Вот тут ошибка
print(list_5)

list_6 = [10, 20, 30, 40, 50]
list_6[1:3] = [90]
print(list_6)
list_6[2:4] = [60, 70, 80]
print(list_6)

list_7 = [1, 2, 3]
list_7.extend([4, 5])
print(list_7) # [1, 2, 3, 4, 5]
list_7.append([4, 5])
print(list_7) # [1, 2, 3, 4, 5, [4, 5]]