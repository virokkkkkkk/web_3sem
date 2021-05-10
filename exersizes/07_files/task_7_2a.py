# -*- coding: utf-8 -*-
"""
Задание 7.2a

Сделать копию скрипта задания 7.2.

Дополнить скрипт:
  Скрипт не должен выводить команды, в которых содержатся слова,
  которые указаны в списке ignore.

Ограничение: Все задания надо выполнять используя только пройденные темы.

"""

from sys import argv

ignore = ["duplex", "alias", "Current configuration"]
# f = argv[1]
f = open('config_sw1.txt')
for line in f:
    # print(len(line.replace('\n','')))
    if (len(line.replace('\n','').replace(' ',''))>0) and (line[0]!='!'):
        # print(line.find(x for x in ignore))
        # print(line.find(ignore[0]))
        flag = True
        for x in ignore:
            if line.find(x)!=-1:
                flag = False
                break
        if flag:
            print(line,end='')