# -*- coding: utf-8 -*-
"""
Задание 7.2c

Переделать скрипт из задания 7.2b:
* передавать как аргументы скрипту:
 * имя исходного файла конфигурации
 * имя итогового файла конфигурации

Внутри, скрипт должен отфильтровать те строки, в исходном файле конфигурации,
в которых содержатся слова из списка ignore.
И записать остальные строки в итоговый файл.

Проверить работу скрипта на примере файла config_sw1.txt.

Ограничение: Все задания надо выполнять используя только пройденные темы.
"""

from sys import argv

ignore = ["duplex", "alias", "Current configuration"]
# f_str = argv[1]
ff_str = argv[2]
# f = open(f_str)
ff = open(ff_str,'w')
f = open('config_sw1.txt')
# ff = open('config_sw1_cleared.txt','w')
for line in f:
    # print(len(line.replace('\n','')))
    if (len(line.replace('\n','').replace(' ',''))>0):
        # print(line.find(x for x in ignore))
        # print(line.find(ignore[0]))
        flag = True
        for x in ignore:
            if line.find(x)!=-1:
                flag = False
                break
        if flag:
            print(line,end='')
            ff.write(line)