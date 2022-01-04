x = 'May 24 12:48:31 ideapad systemd[1]: logrotate.service: Succeeded.'
# 1.1. Выделите и выведите на экран дату и время.
print("task 1.1:")
print(x[0:15])
# 1.2. Выделите и выведите на экран название сервиса (systemd[1]), записавшего лог.
print("task 1.2:")
print(x[24:34])
# 1.3. Замените название ПК (ideapad) на PC-12092, выведите полученную строку на экран.
print("task 1.3:")
print(x.replace('ideapad', 'PC-12092'))
# 1.4. Найдите в логе слово failed и выведите его позицию, если такого слова нет, выведите -1.
print("task 1.4:")
print(x.find('failed'))
# 1.5. Посчитайте количество букв 'S' в строке вне зависимости от регистра (и прописных, и заглавных).
print("task 1.5:")
x15 = x.lower()
print(x15.count('s'))
# 1.6. Выделите из строки значения часов, минут и секунд, суммируйте эти 3 числа и выведите полученное число на экран.
print("task 1.6:")
x4 = x[7:9]
x5 = x[10:12]
x6 = x[13:15]
x7 = int(x4) + int(x5) + int(x6)
print(x7)
print("task 2:")
y = 'May 24 14:03:01 ideapad colord[844]: failed to get session [pid 8279]: Нет доступных данных'
y7 = y.split()
y8 = " ".join(y7[5:9])
y9 = " ".join(y7[11:14])
print(f'The PC "{y7[3]}" receive message from service {y7[4]} what says "{y8}" because "{y9}" at {y7[0]} {y7[1]}, {y7[2]}')
