x = 'May 24 12:48:31 ideapad systemd[1]: logrotate.service: Succeeded.'
# 1.1. Выделите и выведите на экран дату и время.
print(x[0:15])
# 1.2. Выделите и выведите на экран название сервиса (systemd[1]), записавшего лог.
print(x[24:34])
# 1.3. Замените название ПК (ideapad) на PC-12092, выведите полученную строку на экран.
print(x.replace('ideapad', 'PC-12092'))
# 1.4. Найдите в логе слово failed и выведите его позицию, если такого слова нет, выведите -1.
print(x.find('failed'))
# 1.5. Посчитайте количество букв 'S' в строке вне зависимости от регистра (и прописных, и заглавных).
x15 = x.lower()
print(x15.count('s'))
# 1.6. Выделите из строки значения часов, минут и секунд, суммируйте эти 3 числа и выведите полученное число на экран.
x4 = x[7:9]
x5 = x[10:12]
x6 = x[13:15]
x7 = int(x4) + int(x5) + int(x6)
print(x7)
# 2. Вы получили такую строку логов:
# 'May 24 14:03:01 ideapad colord[844]: failed to get session [pid 8279]: Нет доступных данных'
# Нужно сформировать и вывести сообщение в таком формате:
# The PC "<имя ПК>" receive message from service "<имя сервиса>" what says "<сообщение>" because
# "<причина ошибки>" at <дата, время>
y = 'May 24 14:03:01 ideapad colord[844]: failed to get session [pid 8279]: Нет доступных данных'
y1 = y[16:23]
y2 = y[24:30]
y3 = y[71:92]
y4 = y[37:58]
y5 = y[0:6]
y6 = y[7:15]
print(f'The PC "{y1}" receive message from service "{y2}" what says "{y4}" because "{y3}" at {y5} , {y6}')

y7 = y.split()
print(y7)
y8 = " ".join(y7[5:9])
y9 = " ".join(y7[11:14])

print(f' The PC "{y7[3]}" receive message from service {y7[4]} what says "{y8}" because "{y9}" at {y7[0]} {y7[1]}, {y7[2]}')