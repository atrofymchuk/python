# 2. Загрузите в файл с именем 'file_6.txt' строки этого списка за 20 мая

file_1 = open('file_5.txt', 'r')
list = file_1.readlines()
list_1 = []

for a in list:
    list_2 = a.split()
    list_3 = " ".join(list_2[0:2])
    list_4 = " ".join(list_2[2:3])
    list_5 = " ".join(list_2[3:4])
    list_6 = " ".join(list_2[4:5])
    list_7 = list_6.replace(":", "")
    list_8 = " ".join(list_2[5:])
    list_1.append({"date": list_3, "time": list_4, "pc_name": list_5, "service_name": list_7, "message": list_8})

date = "May 20"
list_10 = []

for i in list_1:
    if i['date'] == date:
        list_10 = (i["date"], i["time"], i["pc_name"], i["service_name"], i["message"])
        list_11 = " ".join(list_10[0:])
        with open('file_6.txt', 'a', encoding='cp1251') as file_2:
            file_2.write(list_11)
            file_2.write("\n")
file_1.close
# 3. Считайте из этого файла время первой записи.Ничего кроме времени считывать не нужно! Выведите это время на экран.

file_3 = open("file_6.txt", "r")
list_21 = file_3.readlines()
for a in list_21:
    list_23 = a.split()
    list_24 = " ".join(list_23[2:3])
    print(list_24)
file_3.close


