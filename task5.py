list = [
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
# 2. Создайте из него список словарей, используя ключи из того же задания
list10 = []
y = 0
for a in list:
    list1 = list[y].split()
    y = y + 1
    list2 = " ".join(list1[0:3])
    list3 = " ".join(list1[3:4])
    list4 = " ".join(list1[4:5])
    list6 = list4.replace(":", "")
    list5 = " ".join(list1[5:])
    list10.append({"time": list2, "pc_name": list3, "service_name": list6, "message": list5})

# 3. Выведите на экран список значений <дата/время> всех словарей. Воспользуйтесь списковым включением.
x = 0
print("Task 3 (список значений <дата/время> всех словарей):")
for i in list10:
    print(list10[x]['time'])
    x = x + 1
# 4. Измените словари в списке: создайте новый ключ 'date', перенеся в его значение дату из поля 'time'.
# В поле 'time' оставьте только время. Выведите значения для поля 'time' всех словарей в списке.
z = 0
print("Task 4 (значения для поля 'time' всех словарей в списке):")
for j in list10:
    list11 = list10[z]['time']
    list12 = list11.split()
    list13 = " ".join(list12[0:2])
    list14 = " ".join(list12[2:3])
    list10[z]['time'] = list14
    list10[z]['date'] = list13
    print(list10[z]['time'])
    z = z + 1
# 5. Выведите список значений поля 'message' для всех логов, которые записал ПК с именем 'PC0078'.
# Воспользуйтесь списковым включением.
q = 0
f = "PC0078"
f = str(f)
print("Task 5 (список значений поля 'message' для всех логов, которые записал ПК с именем 'PC0078'):")
for i in list10:
    pc = list10[q]['pc_name']
    pc = str(pc)
    if pc==f:
        print(list10[q]["message"])
    q = q + 1
# 6. Превратите список логов в словарь. Ключами в нем будут целые числа от 100 до 110, а значениями - словари логов.
dict1 = {}
r = 0
l = 100

for k in list10:
    dict1[l] = list10[r]
    r = r + 1
    l = l + 1

# 7. Выведите на экран лог под ключом 104.
print("Task 7 (вывод на экран лог под ключом 104")
print(dict1[104])