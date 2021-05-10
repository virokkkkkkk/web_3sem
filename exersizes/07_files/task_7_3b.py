# -*- coding: utf-8 -*-
"""
Задание 7.3b

Сделать копию скрипта задания 7.3a.

Переделать скрипт:
- Запросить у пользователя ввод номера VLAN.
- Выводить информацию только по указанному VLAN.

Ограничение: Все задания надо выполнять используя только пройденные темы.

"""
import re

d = {}
vlan = input('Введите номер vlan: ')
f = open('CAM_table.txt')
for line in f:
    # print(re.search(r'([0-9A-Fa-f]{4}[.]){2}([0-9A-Fa-f]{4})',line)!=None)
    if re.search(r'([0-9A-Fa-f]{4}[.]){2}([0-9A-Fa-f]{4})',line)!=None:
        v=int(line.split()[0])
        # print(v)
        # print(line, end='')
        d.setdefault(v,line)

# l = list(d.keys())
# l.sort()
# for i in l:
#     print(d[i],end='')

print(d[int(vlan)])