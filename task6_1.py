# 2. Загрузите в файл с именем 'file_6.txt' строки этого списка за 20 мая
file_1 = open('file_5.txt', 'r')
date_1 = "May 20"
for line in file_1:
    date_2 = file_1.read(6)
    if date_2 == date_1:
        with open('file_6.txt', 'a', encoding='cp1251') as file_2:
            str = date_2 + line
            file_2.write(str)
file_1.close()

# 3. Считайте из этого файла время первой записи. Ничего кроме времени считывать не нужно!
# Выведите это время на экран.
file_3 = open('file_6.txt', 'r')
file_3.seek(6)
print(file_3.read(8))
file_3.close()