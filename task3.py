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
# Пример заполнения одной словаря одной строкой
list0 = list[0].split()
dict1 = {
        "time": " ".join(list0[0:3]),
        "pc_name": " ".join(list0[3:4]),
        "service_name": " ".join(list0[4:5]),
        "message": " ".join(list0[5:])
}

# 3. Заполните словарь для одной из строк лога с помощью данного алгоритма, запросив у пользователя номер строки
# с помощью input(). Выведите на экран информацию из текущего словаря в таком виде:
x = input("Укажите номер строки:\n")
x = int(x) - 1
list1 = list[x].split()
serv_name = " ".join(list1[4:5])
`serv_name = serv_name.replace(":", "")`
dict2 = {
        "time": " ".join(list1[0:3]),
        "pc_name": " ".join(list1[3:4]),
        "service_name": serv_name,
        "message": " ".join(list1[5:])
}

x1 = dict2['pc_name']
x2 = dict2['message']

print("Task 3:")
print(f'{x1}: {x2}')

# 4.1. Скопируйте к себе литерал списка:
list_4_1 = ['May 26 12:48:18', 'ideapad', 'systemd[1]', 'Finished Message of the Day.']

# 4.2. Создайте список ключей из пункта 2.
list_4_2 = ['time', 'pc_name', 'service_name', 'message']

# 4.3. Используя функцию zip(), создайте словарь из этих двух списков

dict_4_1 = dict(zip(list_4_2, list_4_1))
print("Task 4.3")
print(dict_4_1)

# 5. Создайте список словарей: из словаря, который вы получили в пункте 3 и словаря из пункта 4
# (в итоге у вас должен получиться список, состоящий из двух словарей). Выведите полученный список на экран
list_5_1 = []
list_5_1.append(dict2)
list_5_1.append(dict_4_1)
print('Task 5:')
print(list_5_1)

# 6. Используя преобразование во множество, выведите список совпадающих значений полученных словарей.
# Что касается п. 6, тут нужно использовать функцию set для преобразования во множество.
# Далее вы используете операцию пересечения множеств &.
# Но учтите, что если вы просто обернете словарь функцией set(), то получите множество ключей.
# Чтобы получить множество значений, используйте также функцию values()
print('Task 6:')
set_1 = list_5_1[0]
set_2 = list_5_1[1]
set_4 = set(set_1.values())
set_5 = set(set_2.values())
set_6 = (set_4 & set_5)
print(set_6)