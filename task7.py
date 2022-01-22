# 2. Напишите функцию, которая:
# 2.1. Получает в качестве первого аргумента список для вывода данных,
# а в качестве последующих - сколько угодно строк логов по типу тех, что есть в скопированном вами списке.
# 2.2. Превращает вводимые вами строки логов в словари по тому же принципу,
# что и в пункте 2 задания для 3го урока. Напоминаю:
# 'time': <дата/время>
# 'pc_name': <имя компьютера>
# 'service_name': <имя сервиса>
# 'message': <сообщение лога>
# 2.3. Модифицирует входной список (переданный в качестве первого аргумента), добавляя в него все созданные словари.
# Возвращать функция, соответственно, должна None

input_list = [
    'May 18 13:06:54 ideapad kwin_x11[1273]: Qt Quick Layouts: Detected recursive rearrange. Aborting after two iterations.',
    'May 20 09:16:28 PC0078 systemd[1]: Starting PackageKit Daemon...',
    'May 20 11:01:12 PC-00102 PackageKit: daemon start',
    'May 20 12:48:18 PC0078 systemd[1]: Starting Message of the Day...',
    'May 21 14:33:55 PC0078 kernel: [221558.992188] usb 1-4: New USB device found, idVendor=1395, idProduct=0025, bcdDevice= 1.00',
    'May 22 11:48:30 ideapad mtp-probe: checking bus 1, device 3: "/sys/devices/pci0000:00/0000:00:08.1/0000:03:00.3/usb1/1-4',
    'May 22 11:50:09 ideapad mtp-probe: bus: 1, device: 3 was not an MTP device',
    'May 23 08:06:14 PC-00233 kernel: [221559.381614] usbcore: registered new interface driver snd-usb-audio',
    'May 24 16:19:52 PC-00233 systemd[1116]: Reached target Sound Card.',
    'May 24 19:26:40 PC-00102 rtkit-daemon[1131]: Supervising 5 threads of 2 processes of 1 users.']
out_list = []
def my_func(out_list, *args):

    for key in args:
        list_0 = key.split()
        dict_1 = {
            "time": " ".join(list_0[0:3]),
            "pc_name": " ".join(list_0[3:4]),
            "service_name": " ".join(list_0[4:5]),
            "message": " ".join(list_0[5:])
        }
        out_list.append(dict_1)
# my_func(out_list, input_list[0], input_list[1], input_list[2])
# print(out_list)
# out_list = []
# out_list_1 = []
# def my_func(out_list, *args):
#
#     for key in args:
#         list_0 = key.split()
#         list_1 = " ".join(list_0[0:3])
#         list_2 = " ".join(list_0[3:4])
#         list_3 = " ".join(list_0[4:5])
#         list_4 = " ".join(list_0[5:])
#         return out_list_1.append({"time": list_1, "pc_name": list_2, "service_name": list_3, "message": list_4})
# print(my_func(out_list, input_list[0], input_list[1], input_list[2]))
# print(my_func())
# 3. Создайте пустой список и добавьте в него 1ю, 2ю и 4ю запись из списка логов с помощью одного вызова вашей функции.
# Выведите полученный список на экран
list_5 = []
my_func(out_list, input_list[0], input_list[1], input_list[3])
for i in range(3):
    list_5.append(out_list[i])

print(list_5)
list_7 = [
    {'id': 382, 'total': 999641890816, 'used': 228013805568},
    {'id': 385, 'total': 61686008768, 'used': 52522710872},
    {'id': 398, 'total': 149023482194, 'used': 83612310700},
    {'id': 400, 'total': 498830397039, 'used': 459995976927},
    {'id': 401, 'total': 93386008768, 'used': 65371350065},
    {'id': 402, 'total': 988242468378, 'used': 892424683789},
    {'id': 430, 'total': 49705846287, 'used': 9522710872},
]
# 5. Напишите функцию, которая:
# 5.1. Получает этот список
# 5.2. Анализирует состояние памяти каждого накопителя по алгоритму из задания для 4го урока. Напоминаю:
# Если свободной памяти осталось меньше 10Гб или меньше 5%, то на накопителе критически мало свободного места;
# Если свободной памяти больше, чем в предыдущем пункте, но меньше 30Гб или меньше 10%,
# то на накопителе мало свободного места;
# Иначе на накопителе достаточно свободного места
# 5.3. Формирует словарь, ключами которого являются: 'memory_ok', 'memory_not_enough' и 'memory_critical',
# а значениями - списки id накопителей, состояние которых относится к соответствующему ключу
# (достаточно свободного места, мало свободного места и критически мало свободного места соответственно).
#
# 5.4. Возвращает сформированный словарь.
memory_ok=[]
memory_not_enough=[]
memory_critical=[]
dict_2 = {'memory_ok': memory_ok, 'memory_not_enough': memory_not_enough, 'memory_critical': memory_critical}
def my_func_1(*args):
    i = 0
    for key in args:
        # print(list_7[i]['total'])
        id_disk = list_7[i]['id']
        # print(id_disk)
        free_mem_number = (list_7[i]['total']) - (list_7[i]['used'])
        free_mem_percent = 100 - (list_7[i]['used']) * 100 / (list_7[i]['total'])
        free_mem_number1 = (round(free_mem_number * 1e-09))
        free_mem_percent1 = (round(free_mem_percent))
        if free_mem_number1 < 10 or free_mem_percent1 < 5:
            print(f'на накопителе {id_disk} критически мало свободного места')
            memory_critical.append(id_disk)
        elif free_mem_number1 > 10 and free_mem_number1 < 30 or free_mem_percent1 > 5 and free_mem_percent1 < 10:
            print(f'на накопителе {id_disk} мало свободного места')
            memory_not_enough.append(id_disk)
        else:
            print(f'на накопителе {id_disk} достаточно свободного места')
            memory_ok.append(id_disk)
        i = i + 1
my_func_1(list_7[0],list_7[1], list_7[2],list_7[3], list_7[4], list_7[5], list_7[6])
# 6.Примените эту функцию к вашему списку и выведите словарь, полученный в результате ее работы, на экран.
print(dict_2)