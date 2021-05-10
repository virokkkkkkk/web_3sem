# -*- coding: utf-8 -*-
"""
Задание 11.1

Создать функцию parse_cdp_neighbors, которая обрабатывает вывод команды show cdp neighbors.

У функции должен быть один параметр command_output, который ожидает как аргумент вывод команды одной строкой (не имя файла). Для этого надо считать все содержимое файла в строку,
а затем передать строку как аргумент функции (как передать вывод команды показано в коде ниже).

Функция должна возвращать словарь, который описывает соединения между устройствами.

Например, если как аргумент был передан такой вывод:
R4>show cdp neighbors

Device ID    Local Intrfce   Holdtme     Capability       Platform    Port ID
R5           Fa 0/1          122           R S I           2811       Fa 0/1
R6           Fa 0/2          143           R S I           2811       Fa 0/0

Функция должна вернуть такой словарь:

    {("R4", "Fa0/1"): ("R5", "Fa0/1"),
     ("R4", "Fa0/2"): ("R6", "Fa0/0")}

В словаре интерфейсы должны быть записаны без пробела между типом и именем. То есть так Fa0/0, а не так Fa 0/0.

Проверить работу функции на содержимом файла sh_cdp_n_sw1.txt. При этом функция работать
и на других файлах (тест проверяет работу функции на выводе из sh_cdp_n_sw1.txt и sh_cdp_n_r3.txt).

Ограничение: Все задания надо выполнять используя только пройденные темы.
"""


def parse_cdp_neighbors(command_output):
    """
    Тут мы передаем вывод команды одной строкой потому что именно в таком виде
    будет получен вывод команды с оборудования. Принимая как аргумент вывод
    команды, вместо имени файла, мы делаем функцию более универсальной: она может
    работать и с файлами и с выводом с оборудования.
    Плюс учимся работать с таким выводом.
    """
    d = {}
    # print(command_output)
    Lines = command_output.split('\n')
    # firstDevice = ''
    # Флаг, показывающий, что началось перечисление строк с нужной информацией
    IsReadyToRead = False
    for line in Lines:
        # print(line.strip())
        if(len(line.strip())>0):
            if('>show cdp neighbors' in line):
                firstDevice = line[0:line.find('>show cdp neighbors')]
                # print(firstDevice)
            if IsReadyToRead :
                mylist = line.split()
                Device = mylist[0]
                LocalInt = mylist[1]+mylist[2]
                PortID = mylist[-2] + mylist[-1]
                d[firstDevice, LocalInt] = Device,PortID
                # print(list(firstDevice).append(LocalInt))
                # print(Device, LocalInt, PortID)
            if('Device ID' in line):
                IsReadyToRead = True
    return d

if __name__ == "__main__":
    with open("sh_cdp_n_sw1.txt") as f:
        print(parse_cdp_neighbors(f.read()))
