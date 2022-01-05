# 1. Скопируйте их к себе и создайте из них список (список строк).
list = ['May 18 13:06:54 ideapad kwin_x11[1273]: Qt Quick Layouts: Detected recursive rearrange. Aborting after two iterations.',
         'May 20 09:16:28 PC0078 systemd[1]: Starting PackageKit Daemon...',
         'May 20 11:01:12 PC-00102 PackageKit: daemon start',
         'May 20 12:48:18 PC0078 systemd[1]: Starting Message of the Day...',
         'May 21 14:33:55 PC0078 kernel: [221558.992188] usb 1-4: New USB device found, idVendor=1395, idProduct=0025, bcdDevice= 1.00',
         'May 22 11:48:30 ideapad mtp-probe: checking bus 1, device 3: "/sys/devices/pci0000:00/0000:00:08.1/0000:03:00.3/usb1/1-4',
         'May 22 11:50:09 ideapad mtp-probe: bus: 1, device: 3 was not an MTP device',
         'May 23 08:06:14 PC-00233 kernel: [221559.381614] usbcore: registered new interface driver snd-usb-audio',
         'May 24 16:19:52 PC-00233 systemd[1116]: Reached target Sound Card.',
         'May 24 19:26:40 PC-00102 rtkit-daemon[1131]: Supervising 5 threads of 2 processes of 1 users.']

list0 = list[0].split()
list1 = list[1].split()
list2 = list[2].split()
list3 = list[3].split()
list4 = list[4].split()
list5 = list[5].split()
list6 = list[6].split()
list7 = list[7].split()
list8 = list[8].split()
list9 = list[9].split()

dict1 = {
    "1": {
        "time": " ".join(list0[0:3]),
        "pc_name": " ".join(list0[3:4]),
        "service_name": " ".join(list0[4:5]),
        "message": " ".join(list0[5:])
    },
    "2": {
        "time": " ".join(list1[0:3]),
        "pc_name": " ".join(list1[3:4]),
        "service_name": " ".join(list1[4:5]),
        "message": " ".join(list1[5:])
    },
    "3": {
        "time": " ".join(list2[0:3]),
        "pc_name": " ".join(list2[3:4]),
        "service_name": " ".join(list2[4:5]),
        "message": " ".join(list2[5:])
    },
    "4": {
        "time": " ".join(list3[0:3]),
        "pc_name": " ".join(list3[3:4]),
        "service_name": " ".join(list3[4:5]),
        "message": " ".join(list3[5:])
    },
    "5": {
        "time": " ".join(list4[0:3]),
        "pc_name": " ".join(list4[3:4]),
        "service_name": " ".join(list4[4:5]),
        "message": " ".join(list4[5:])
    },
}
#print('Task 2:')
#print(dict1)

# 3. Заполните словарь для одной из строк лога с помощью данного алгоритма, запросив у пользователя номер строки с помощью input(). Выведите на экран информацию из текущего словаря в таком виде:
x = input("Укажите номер строки\n")
y = dict1[x]
#print(y)

# 4.1. Скопируйте к себе литерал списка:
list_4_1 = ['May 26 12:48:18', 'ideapad', 'systemd[1]', 'Finished Message of the Day.']

# 4.2. Создайте список ключей из пункта 2.
list_4_2 = ['time', 'pc_name', 'service_name', 'message']

# 4.3. Используя функцию zip(), создайте словарь из этих двух списков

dict_4_1 = dict(zip(list_4_2, list_4_1))
print("Task 4.3")
print(dict_4_1)
# 5. Создайте список словарей: из словаря, который вы получили в пункте 3 и словаря из пункта 4 (в итоге у вас должен получиться список, состоящий из двух словарей). Выведите полученный список на экран
list_5_1 = []
list_5_1.append(y)
list_5_1.append(dict_4_1)
print('Task 5:')
print(list_5_1)
#
# # 6. Используя преобразование во множество, выведите список совпадающих значений полученных словарей.
# Что касается п. 6, тут нужно использовать функцию set для преобразования во множество.
# Далее вы используете операцию пересечения множеств &.
# Но учтите, что если вы просто обернете словарь функцией set(), то получите множество ключей.
# Чтобы получить множество значений, используйте также функцию values()
# print('Task 6:')
