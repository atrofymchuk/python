# 1. Скопируйте их к себе и создайте из них список (список строк).
# May 18 13:06:54 ideapad kwin_x11[1273]: Qt Quick Layouts: Detected recursive rearrange. Aborting after two iterations.
# May 20 09:16:28 PC0078 systemd[1]: Starting PackageKit Daemon...
# May 20 11:01:12 PC-00102 PackageKit: daemon start
# May 20 12:48:18 PC0078 systemd[1]: Starting Message of the Day...
# May 21 14:33:55 PC0078 kernel: [221558.992188] usb 1-4: New USB device found, idVendor=1395, idProduct=0025, bcdDevice= 1.00
# May 22 11:48:30 ideapad mtp-probe: checking bus 1, device 3: "/sys/devices/pci0000:00/0000:00:08.1/0000:03:00.3/usb1/1-4"
# May 22 11:50:09 ideapad mtp-probe: bus: 1, device: 3 was not an MTP device
# May 23 08:06:14 PC-00233 kernel: [221559.381614] usbcore: registered new interface driver snd-usb-audio
# May 24 16:19:52 PC-00233 systemd[1116]: Reached target Sound Card.
# May 24 19:26:40 PC-00102 rtkit-daemon[1131]: Supervising 5 threads of 2 processes of 1 users.

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

# 2. Создайте алгоритм заполнения словаря, подходящий для любой строчки лога.
# Словарь должен содержать в себе такую информацию:
# 'time': <дата/время>
# 'pc_name': <имя компьютера>
# 'service_name': <имя сервиса>
# 'message': <сообщение лога>
# Еще раз обращаю ваше внимание на то, что алгоритм заполнения должен быть универсальным для всех данных строк.
dict1 = {'time': '', 'pc_name': '','service_name': '', 'message': ''}
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

dict1['time'] = " ".join(list0[2:3]), " ".join(list1[2:3]), " ".join(list2[2:3]), " ".join(list3[2:3]), " ".join(list4[2:3]), " ".join(list5[2:3]), " ".join(list6[2:3]), " ".join(list7[2:3]), " ".join(list8[2:3]), " ".join(list9[2:3])
dict1['pc_name'] = " ".join(list0[3:4]), " ".join(list1[3:4]), " ".join(list2[3:4]), " ".join(list3[3:4]), " ".join(list4[3:4]), " ".join(list5[3:4]), " ".join(list6[3:4]), " ".join(list7[3:4]), " ".join(list8[3:4]), " ".join(list9[3:4])
dict1['service_name'] = " ".join(list0[4:5]), " ".join(list1[4:5]), " ".join(list2[4:5]), " ".join(list3[4:5]), " ".join(list4[4:5]), " ".join(list5[4:5]), " ".join(list6[4:5]), " ".join(list7[4:5]), " ".join(list8[4:5]), " ".join(list9[4:5])
dict1['message'] = " ".join(list0[5:]), " ".join(list1[5:]), " ".join(list2[5:]), " ".join(list3[5:]), " ".join(list4[5:]), " ".join(list5[5:]), " ".join(list6[5:]), " ".join(list7[5:]), " ".join(list8[5:]), " ".join(list9[5:])


print(dict1)